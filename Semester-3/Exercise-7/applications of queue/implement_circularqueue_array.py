class CircularQueue:
    def __init__(self,size=100):
        self.size=size
        self.a=[None]*self.size
        self.front=-1
        self.rear=-1
    def is_empty(self):
        return self.front==-1
    def enqueue(self,data):
        if(self.front==-1 and self.rear==-1):
            self.front=0
            self.rear=0
            self.a[self.rear]=data
        elif((self.rear+1)%(self.size)==self.front):
            print("Queue is Overflow")     
        else:
            self.rear=(self.rear+1)%self.size
            self.a[self.rear]=data

    def dequeue(self):
        if(self.front!=-1 and self.rear==-1):
            return "Queue is Underflow"
        elif(self.front==self.rear):
            temp=self.a[self.front]
            self.front=-1
            self.rear=-1
            
        else:
            temp=self.a[self.front]    
            self.front=(self.front+1)%self.size
        return temp
    def get_front(self):
        if(self.is_empty()):
            return "Queue is empty"
        return self.a[self.front]    
    def get_rear(self):
        if(self.is_empty()):
            return "Queue is empty"
        return self.a[self.rear]    

    def display(self):
        if(self.front==-1):
            print("Queue is empty")
        else:
            temp=self.front
            while(temp!=self.rear):
                print(self.a[temp],end=" ")
                temp=(temp+1)%self.size
            print(self.a[temp])
size=int(input("Enter size of the circular queue:"))
cq=CircularQueue(size)
print("--------------------------")
print("\n1.Enqueue\n2.Dequeue\n3.Get front\n4.Get Rear\n5.check empty or not\n6.Display Queue\n7.Exit")
print("--------------------------")
while(1):
    # print("--------------------------")
    # print("\n1.Enqueue\n2.Dequeue\n3.Get front\n4.Get Rear\n5.check empty or not\n6.Display Queue\n7.Exit")
    # print("--------------------------")
    c=int(input("Enter your choice(1/2/3/4/5/6/7):"))
    if(c==1):
        data=int(input("Enter element to insert into queue:"))
        cq.enqueue(data)
    elif(c==2):
        print("Dequeued value:",cq.dequeue())
    elif(c==3):
        print("Front value:",cq.get_front())
    elif(c==4):
        print("Rear value:",cq.get_rear())
    elif(c==5):
        print("Queue is empty:",cq.is_empty())
    elif(c==6):
        cq.display()
    elif(c==7):
        break
    else:
        print("Invalid Input")        

