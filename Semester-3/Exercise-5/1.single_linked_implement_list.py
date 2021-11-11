class CreateNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None if True else False

    def len(self):
        temp = self.head
        i = 0
        while(temp != None):
            temp = temp.next
            i += 1
        return i

    def pos(self, data):
        current = self.head
        while(current != None and current.data != data):
            current = current.next
        return current

    def pos_before(self, data):
        current = self.head
        while(current.next != None and current.next.data != data):
            current = current.next
        if(current.next.data):
            return current
        return

    def pos_after(self, data):
        current = self.head
        while(current.next != None and current.data != data):
            current = current.next
        return current.next

    def add_first(self, data):
        newnode = CreateNode(data)
        newnode.next = self.head
        self.head = newnode

    def add_before(self, p, data):
        newnode = CreateNode(data)
        if(self.head.data == p):
            newnode.next = self.head
            self.head = newnode
            return
        pre_node = self.pos_before(p)
        newnode.next = pre_node.next
        pre_node.next = newnode

    def add_after(self, p, data):
        current_node = self.pos(p)
        newnode = CreateNode(data)
        newnode.next = current_node.next
        current_node.next = newnode

    def add_last(self, data):
        newnode = CreateNode(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newnode

    def delete_first(self):
        if(self.is_empty()):
            print("\n\"Linked list is empty\"\n")
        elif(self.head.next == None):
            self.head = None
        else:
            temp = self.head
            self.head = temp.next
            temp = None

    def delete_last(self):
        temp = self.head
        if(self.is_empty()):
            print("\n\"Linked list is empty\"\n")
        elif(temp.next == None):
            self.head = None
        else:
            while(temp.next != None and temp.next.next != None):
                temp = temp.next
            temp.next = None

    def delete_specified(self, data):
        temp = self.head
        if(self.is_empty()):
            print("\n\"Linked list is empty\"\n")
        elif(temp.next == None and temp.data != data):
            print("Given data not in the list")
        elif(temp.data == data):
            self.delete_first()
        else:
            temp = self.pos_before(data)
            if(not temp):
                print("Given data not in the list")
                return
            if(temp.next.next):
                temp.next = temp.next.next
            else:
                temp.next = None

    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data, "-->", end=" ")
            temp = temp.next
        print("None")

print("\n------------------------------------\n")
print("1.Add first\n2.Add last\n3.Add after\n4.Add before\n5.Delete first\n6.Delete specified node\n7.Delete last\n8.Is Empty\n9.Find Length\n10.Display list\n11.Exit")
print("\n------------------------------------\n")
l = LinkedList()
while(1):
    c = int(input("Enter your choice:"))
    if(c == 1):
        data = int(input("Enter the data:"))
        l.add_first(data)
    elif(c == 2):
        data = int(input("Enter the data:"))
        l.add_last(data)
    elif(c == 3):
        pos = int(input("Add after:"))
        data = int(input("Enter the data to add node:"))
        l.add_after(pos, data)
    elif(c == 4):
        pos = int(input("Add before:"))
        data = int(input("Enter the data to add node:"))
        l.add_before(pos, data)
    elif(c == 5):
        l.delete_first()
    elif(c == 6):
        data = int(input("Enter the data for which the node is to be deleted:"))
        l.delete_specified(data)
    elif(c == 7):
        l.delete_last()
    elif(c == 8):
        print("List is empty:", l.is_empty())
    elif(c == 9):
        print("length of the list:", l.len())
    elif(c == 10):
        l.display()
    elif(c == 11):
        break
    else:
        print("Invalid Input")
