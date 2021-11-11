class Queue:
    def __init__(self):
        self.a=[]
    def is_empty(self):
        return len(self.a)==0
    def enqueue(self,data):
        self.a.append(data)
    def dequeue(self):
        if(self.is_empty()):
            return "No element in the queue"
        else:
            return self.a.pop(0)
    def first(self):
        if(self.is_empty()):
            return "No element in the queue"
        else:
            return self.a[0]
q=Queue()
while(1):
    print("Operations:\n1.Enqueue\n2.Dequeue\n3.First\n4.check empty or not\n5.Find length\n6.Exit")
    c=int(input("Enter your choice(1/2/3/4/5/6):"))
    if(c==6):
        break
    if(c==1):
        data=int(input("Enter a value to enqueue into the queue:"))
        q.enqueue(data)
    elif(c==2):
        print("Dequeued element:",q.dequeue())  
    elif(c==3):
        print("First element:",q.first())  
    elif(c==4):
        print("Queue is empty(True/false):",q.is_empty()) 
    elif(c==5):
        print("Length of the queue:",len(q.a))
    else:
        print("Invalid Input")                                      
