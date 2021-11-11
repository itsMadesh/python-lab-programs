class Stack:
    def __init__(self):
        self.a=[]
        self.top_=-1
    def is_empty(self):
        return len(self.a)==0    
    def push(self,data):
        self.a.append(data)
        self.top_+=1
    def pop(self):
        if(self.top_==-1):
            return "No element in the stack"
        else:
            self.top_-=1
            return self.a.pop()   
    def top(self):
        if(self.top_==-1):
            return "No element in the stack" 
        else:
            return self.a[-1]  