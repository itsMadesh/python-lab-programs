class Stack:
    def __init__(self):
        self.a=[]
    def is_empty(self):
        return len(self.a)==0    
    def push(self,data):
        self.a.append(data)
    def pop(self):
        if(len(self.a)<=0):
            return "No element in the stack"
        else:
            return self.a.pop()   
    def top(self):
        if(len(self.a)<=0):
            return "No element in the stack" 
        else:
            return self.a[-1]  
s=Stack()                       
while(1):
    print("Operations:\n1.Push\n2.Pop\n3.Top\n4.check empty or not\n5.Find length\n6.Exit")
    c=int(input("Enter your choice(1/2/3/4/5/6):"))
    if(c==6):
        break
    if(c==1):
        data=int(input("Enter a value to push into the stack:"))
        s.push(data)
    elif(c==2):
        print("popped element:",s.pop())  
    elif(c==3):
        print("Top element:",s.top())  
    elif(c==4):
        print("Stack is empty(True/false):",s.is_empty()) 
    elif(c==5):
        print("Length of the stack:",len(s.a))
    else:
        print("Invalid Input")              
    