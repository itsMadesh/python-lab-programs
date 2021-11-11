class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def count_nodes(self, temp):
        if(temp == None):
            return 0
        return 1+self.count_nodes(temp.next)

    def display(self):
        current = self.head
        while(current):
            print(current.data, "-->", end=" ")
            current = current.next
        print("\n")
        
print("\n----------------\n")
print("1.Add Node\n2.Count Nodes\n3.Display Linkedlist\n4.Exit")
print("\n----------------\n")
l = LinkedList()
while(1):
    # print("\n----------------\n")
    # print("1.Add Node\n2.Count Nodes\n3.Display Linkedlist\n4.Exit")
    # print("\n----------------\n")
    c = int(input("Enter your choice:"))
    if(c == 1):
        data = int(input("Enter the data to insert:"))
        l.insert(data)
    elif(c == 2):
        print("Number of nodes:", l.count_nodes(l.head))
    elif(c == 3):
        l.display()
    elif(c == 4):
        break
    else:
        print("Invalid Input")
