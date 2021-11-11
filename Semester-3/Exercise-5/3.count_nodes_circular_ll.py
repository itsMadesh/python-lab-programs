class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinked:
    def __init__(self):
        self.head = None

    def Insert_first(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.head.next = newnode
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newnode
            newnode.next = self.head
            self.head = newnode

    def Insert_last(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.head.next = newnode
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newnode
            newnode.next = self.head

    def Delete_first(self):
        if self.head is None:
            print("Circular Linked list is empty")
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

    def Delete_last(self):
        if self.head is None:
            print("Circular Linked list is empty")
        else:
            temp = self.head
            if(temp.next == self.head):
                self.head = None
            else:
                while(temp.next and temp.next.next != self.head):
                    temp = temp.next
                temp.next = self.head

    def count_nodes(self):
        if self.head is None:
            return 0
        count = 1
        temp = self.head
        while(temp.next != self.head):
            temp = temp.next
            count += 1
        return count

    def Display_list(self):
        if self.head is None:
            print("Circular linked list is empty")
        else:
            temp = self.head
            while(temp.next != self.head):
                print(temp.data, "--->", end=" ")
                temp = temp.next
            print(temp.data, "--->")

print("\n=======================\n")
print("1.Insert Node at First\n2.Insert Node at Last\n3.Delete Node at First\n4.Delete Node at last\n5.Display list\n6.Count Nodes\n7.Exit")
print("\n========================\n")
cl = CircularLinked()
while(1):
    # print("\n=======================\n")
    # print("1.Insert Node at First\n2.Insert Node at Last\n3.Delete Node at First\n4.Delete Node at last\n5.Display list\n6.Count Nodes\n7.Exit")
    # print("\n========================\n")
    c = int(input("Enter your choice:"))
    if(c == 1):
        data = int(input("Enter the data to be inserted into the list at first:"))
        cl.Insert_first(data)
    elif(c == 2):
        data = int(
            input("Enter the data which to be inserted into the list at last:"))
        cl.Insert_last(data)
    elif(c == 3):
        cl.Delete_first()
    elif(c == 4):
        cl.Delete_last()
    elif(c == 5):
        cl.Display_list()
    elif(c == 6):
        print("Number of Nodes:", cl.count_nodes())
    elif(c == 7):
        break
    else:
        print("Invalid Input")
