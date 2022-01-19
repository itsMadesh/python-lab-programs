class priority_queue:
    def __init__(self, size):
        self.arr = [0] * size
        self.max = size
        self.size = -1
    def parent(self, pos):
        return (pos - 1) // 2

    def lchild(self, pos):
        return 2 * pos + 1

    def rchild(self, pos):
        return 2 * pos + 2
    def get_min(self):
        if self.size==-1:
            return "No element in the heap"
        return self.arr[0]
    def swap(self, pos1, pos2):
        self.arr[pos1], self.arr[pos2] = self.arr[pos2], self.arr[pos1]

    def shiftup(self, current):
        while self.arr[self.parent(current)] > self.arr[current]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    def shiftdown(self,current):
        temp=current
        l=self.lchild(current)
        r=self.rchild(current)
        if(l<self.size and self.arr[temp]>self.arr[l]):
            temp=l
        if(r<self.size and self.arr[temp]>self.arr[r]):
            temp=r
        if(current!=temp):
            self.swap(current,temp)
            self.shiftdown(temp)
    def insert(self, value):
        if self.size >= self.max:
            return
        self.size += 1
        self.arr[self.size] = value
        self.shiftup(self.size)
    def delete_min(self):
        if self.size==-1:
            return
        popped_value=self.arr[0]
        self.arr[0]=self.arr[self.size]
        self.arr[self.size]=0
        self.size-=1
        self.shiftdown(0)
        return popped_value
    def print_queue(self):
        for i in range(0,(self.size//2)+1,1):
            print(" Parent : "+ str(self.arr[i])+" left child : "+
                                str(self.arr[2 * i+1])+" Right child: "+
                                str(self.arr[2 * i + 2]))
n=int(input("Enter priority Queue size:"))
pq=priority_queue(n)
while(1):
    print("1.Insert value\n2.Delete minimum\n3.Get minimum\n4.Print priority Queue\n5.Exit")
    c=int(input("Enter your choice(1/2/3/4/5):"))
    if(c==1):
        value=int(input("Enter value to insert:"))
        pq.insert(value)
    elif(c==2):
        print("Deleted value:",pq.delete_min())
    elif(c==3):
        print("Minimum value in priority queue is:",pq.get_min())
    elif(c==4):
        pq.print_queue()
    elif(c==5):
        break
    else:
        print("Invalid input")


