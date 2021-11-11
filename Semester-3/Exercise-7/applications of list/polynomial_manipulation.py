class Node:
    def __init__(self,coe,pow):
        self.coe=coe
        self.pow=pow
        self.next=None
class create_poly:
        def __init__(self):
            self.head=None
            self.tail=None
        def add_node(self,coe,pow):
            newnode=Node(coe,pow)
            if(self.head is None):
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
        def show_poly(self,temp):
            if(temp==None):
                print("No Nodes in the linked list")
                return
            while(temp.next!=None):
                print(str(temp.coe)+"x^"+str(temp.pow)+"+",end="")
                temp=temp.next
            print(str(temp.coe)+"x^"+str(temp.pow))
        def adding_polynomials(self,p1,p2):
            while(p1 and p2):
                if(p1.pow==p2.pow):
                    self.add_node(p1.coe+p2.coe,p1.pow)
                    p1=p1.next
                    p2=p2.next
                elif(p1.pow>p2.pow):
                    self.add_node(p1.coe,p1.pow)
                    p1=p1.next
                else:
                    self.add_node(p2.coe,p2.pow)
                    p2=p2.next
            while(p1 or p2):
                if(p1):
                    self.add_node(p1.coe,p1.pow)
                    p1=p1.next
                if(p2):
                    self.add_node(p2.coe,p2.pow)
                    p2=p2.next               
            print("p1+p2=",end="")
            self.show_poly(self.head)
p1=create_poly()
p2=create_poly()
print("\n-------------------------\n")
print("\n1.Add node into poly-1\n2.Add node into poly-2\n3.Addind two polynomials\n4.show polynomial equation\n5.Exit")
print("\n-------------------------\n")
while(1):
    # print("\n-------------------------\n")
    # print("\n1.Add node into poly-1\n2.Add node into poly-2\n3.Addind two polynomials\n4.show polynomial equation\n5.Exit")
    # print("\n-------------------------\n")
    c=int(input("Enter your choice:"))
    if(c==1):
        coe=int(input("Enter coefficient:"))
        pow=int(input("Enter power of X:"))
        p1.add_node(coe,pow)
    elif(c==2):
        coe=int(input("Enter coefficient:"))
        pow=int(input("Enter power of X:"))
        p2.add_node(coe,pow)
    elif(c==3):
        add=create_poly()
        add.adding_polynomials(p1.head,p2.head)
    elif(c==4):
        p1.show_poly(p1.head)
        p2.show_poly(p2.head)
    elif(c==5):
        break
    else:
        print("Invalid Input")