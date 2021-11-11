class Queue:
    def __init__(self,size=100):
        self.a=[size]
    def is_empty(self):
        return len(self.a)==0
    def enqueue(self,data):
        self.a.append(data)
    def dequeue(self):
        if(self.is_empty()):
            return None
        else:
            return self.a.pop(0)
    def display(self):
        return self.a
    def first(self):
        if(self.is_empty()):
            return None
        else:
            return self.a[0]