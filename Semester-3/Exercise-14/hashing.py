import sympy
class key_value:
  def __init__(self,key,val,next = None):
    self.key = key
    self.value = val
    self.next = None

class hashtable:
  def __init__(self,size):
    self.size = size
    self.table = [None]*size
  
  def hash_index1(self,key):
    prime = self.size
    while not sympy.isprime(prime):
      prime-=1
    return (prime - (key%prime))

  def isFull(self):
    for i in self.table:
      if i is None:
        return False
    return True

  def clear(self):
    self.table = [None]*self.size
  def hash_index(self,key):
    return key%self.size
    
  def hash_insert(self,key,val,mode=None):
    if not self.isFull():
      addend = key_value(key,val)
      if mode is None:
        self.table[self.hash_index(addend.key)] = addend
      elif mode.upper() == 'C':
        self.chaining(key,val)
      elif mode.upper() == 'L':
        self.table[self.lprobing(key)] = addend
      elif mode.upper() == 'Q':
        self.table[self.qprobing(key)] = addend
      elif mode.upper() == 'D':
        self.table[self.double_hash(key)] = addend
      else:
        print('Technique Invalid')
    else:
      print('Hash_table full!!')

  def double_hash(self,key,val=None):
      position = self.hash_index(key)
      flag =0
      i=0
      while self.table[position] is not None and position<self.size :
        position = (self.hash_index(key) + self.hash_index1(key)*i)%self.size
        i+=1
        if position == self.size and flag == 0:
          position=0
          flag = 1
      return position    

  def print_hash(self):
    for i in self.table:
      if i is None:
        print(i,end=' ')
      else:
        print(i.key,end=' ')
    print()
  
  def chaining(self,key,val):
      key_v = key_value(key,val)
      position = self.hash_index(key)
      if self.table[position] is not None:
        old =  self.table[position]
        while old.next is not None:
          old = old.next
        old.next = key_v
      else:
        self.table[position] = key_v

  def search(self,key,mode=None):
    position = self.hash_index(key)
    old =  self.table[position]
    while old is not None and old.key != key  :
      old = old.next
    if old is not None and old.key == key:
      return old.value
    elif mode.upper() == 'L':
      position = self.hash_index(key)
      i,flag = 0,0
      while self.table[position].key!=key and position<self.size:
        position = self.hash_index(key+i)
        i+=1
        if position == self.size and flag == 0:
          position=0
          flag = 1
      return self.table[position].value
    elif mode.upper() == 'Q':
      position = self.hash_index(key)
      i,flag = 0,0
      while self.table[position].key!=key and position<self.size:
        position = self.hash_index(key+(i**2))
        i+=1
        if position == self.size and flag == 0:
          position=0
          flag = 1
      return self.table[position].value
    elif mode.upper() == 'D':
      position = self.hash_index(key)
      flag =0
      i=0
      while self.table[position].key!= key and position<self.size :
        position = (self.hash_index(key) + self.hash_index1(key)*i)%self.size
        i+=1
        if position == self.size and flag == 0:
          position=0
          flag = 1
      return self.table[position].value
  
  def lprobing(self,key):
      position = self.hash_index(key)
      flag =0
      i=0
      while self.table[position] is not None and position<self.size :
        position = self.hash_index(key+i)
        i+=1
        if position == self.size and flag == 0:
          position=0
          flag = 1
      return position

  def qprobing(self,key):
      position = self.hash_index(key)
      flag =0
      i=0
      while self.table[position] is not None and position<self.size :
        position = self.hash_index(key+(i**2))
        i+=1
        if position == self.size and flag == 0:
          position=0
          flag = 1
      return position

a = hashtable(10)
a.hash_insert(9,12,'c')
a.hash_insert(21,44,'c')
a.hash_insert(78,4,'c')
a.hash_insert(34,1,'c')
a.hash_insert(23,'madesh','c')
a.hash_insert(32,'Dravid','c')
a.hash_insert(12,'antony','c')
a.print_hash()
print('Key 27 sought using linear probing: ',a.search(23,'l'))

a.clear()
print('Using Separate chaining')
a.hash_insert(9,12,'c')
a.hash_insert(21,44,'c')
a.hash_insert(78,4,'c')
a.hash_insert(34,1,'c')
a.hash_insert(23,'madesh','c')
a.hash_insert(32,'Dravid','c')
a.hash_insert(12,'antony','c')
a.print_hash()
print('Key 32 sought using separate chaining: ',a.search(32,'c'))

a.clear()
print('Using Quadratic probing')
a.hash_insert(9,12,'c')
a.hash_insert(21,44,'c')
a.hash_insert(78,4,'c')
a.hash_insert(34,1,'c')
a.hash_insert(23,'madesh','c')
a.hash_insert(32,'Dravid','c')
a.hash_insert(12,'antony','c')
a.print_hash()
print('Key 33 sought using Quadratic probing: ',a.search(12,'q'))

a.clear()
print('Using Double hashing')
a.hash_insert(9,12,'c')
a.hash_insert(21,44,'c')
a.hash_insert(78,4,'c')
a.hash_insert(34,1,'c')
a.hash_insert(23,'madesh','c')
a.hash_insert(32,'Dravid','c')
a.hash_insert(12,'antony','c')
a.print_hash()
print('Key 12 sought using Double hashing: ',a.search(9,'d'))
