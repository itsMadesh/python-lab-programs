import array as arr
class List:
    def  __init__(self):
        self.size=100
        a=[0]*self.size
        self.l=arr.array('i',a)
        self.i=0
    def append(self,data):
        self.l[self.i]=data
        self.i+=1
    def count(self,data):                
        return  sum([1 for x in range(self.i) if(self.l[x]==data)])
    def insert(self,position,data):
        if(self.i<position):
            position=self.i
        self.size+=5
        a=[0]*self.size
        l1=arr.array('i',a)
        y=0   
        for y in range((self.i)+1):
            if(position==y):
                l1[y]=data
                y+=1
                break
            l1[y]=self.l[y]
        for x in range(position,self.i,1):        
            l1[y]=self.l[x]  
            y+=1  
        self.l=l1
        self.i+=1
    def pop(self,position=None):
        if(self.i==0):
            return "No element in the list"
        elif(position==None):
            data=self.l[self.i-1]
            self.l[self.i-1]=0     
        else:
            data=self.l[position]    
            for x in range(position,self.i):
                self.l[x]=self.l[x+1]
        self.i-=1    
        return data
    def remove(self,data):
        for i in range(self.i):
            if(self.l[i]==data):
                self.pop(i)
                return
    def display(self):
        return ([ self.l[x] for x in range(self.i)])
l=List()
while(1):
    print("Methods:\n1.Append\n2.Insert\n3.Pop\n4.Remove\n5.Count\n6.Display list\n7.Exit")
    c=int(input("Enter your choice(1/2/3/4/5/6/7):"))
    if(c==7):
        break
    elif(c==1):
        data=int(input("Enter element:"))
        l.append(data)
    elif(c==2):
        data=int(input("Enter element:"))
        position=int(input("And enter position:"))
        l.insert(position,data)
    elif(c==3):
        position=int(input("Enter position of an element:"))
        print("Popped element:",l.pop(position))  
    elif(c==4):
        data=int(input("Enter element:"))
        l.remove(data)
    elif(c==5):
        data=int(input("Enter an element to count that occurences in the list:"))
        print("Total no.of occurence",data,"=",l.count(data))
    elif(c==6):
        print("List:",l.display())
    else:
        print("Invalid Input")     