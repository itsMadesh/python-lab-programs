# 2. Provide a command-line interface to experiment with the BST.
# (a) s followed by a number should search for the number as the key in the BST and print the number, if found; print nothing, otherwise.
# (b) i followed by a number should insert the number as a new key in the BST. Print the tree after insertion.
# (c) d followed by a number should delete the given key from the BST and print the tree after deletion.
# (d) m should print the minimum key of the BST, and M should print the maximum key of the BST.
# (e) p should print the BST.
# (f) x exits the program.


class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BST_Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, temp, data):
        if temp is None:
            return Node(data)
        elif temp.data > data:
            temp.left = self.insert_node(temp.left, data)
        else:
            temp.right = self.insert_node(temp.right, data)
        return temp

    def delete_node(self, current, data):
        if current is None:
            return current
        elif current.data > data:
            current.left = self.delete_node(current.left, data)
        elif current.data < data:
            current.right = self.delete_node(current.right, data)
        else:
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp
            temp = current.right
            while temp.left is not None:
                temp = temp.left
            current.data = temp.data
            current.right = self.delete_node(current.right, temp.data)
        return current

    def search(self, temp, data):
        if temp == None or temp.data == data:
            return temp
        elif temp.data > data:
            return self.search(temp.left, data)
        else:
            return self.search(temp.right, data)

    def FindMin(self):
        temp = self.root
        if temp is None:
            return "No elements in the tree"
        else:
            while temp.left is not None:
                temp = temp.left
            return temp.data

    def FindMax(self):
        temp = self.root
        if temp is None:
            return "No elements in the tree"
        else:
            while temp.right is not None:
                temp = temp.right
            return temp.data

    def print_tree(self, temp):
        if temp is None:
            return -1
        self.print_tree(temp.left)
        print(temp.data,end=" ")
        self.print_tree(temp.right)


def show_choices():
    print("\nOperations:")
    print("----------------------------\n")
    print("'s'-Search element in the tree")
    print("'i'-Insert an element into the tree")
    print("'d'-delete an element from the tree")
    print("'m'-Print the minimum element from the tree")
    print("'M'-Print the maximum element from the key")
    print("'p'-Print the BST")
    print("'x'-Exits the program")
    print("'show'-Show operations")
    print("\n----------------------------\n")
t1 = BST_Tree()
show_choices()
while(1):
    c = input("\nEnter your choice(s/i/d/m/M/p/x/show):")
    if(c == "s"):
        data = int(input("Enter an element to search:"))
        print(data,
            "Found in " if (t1.search(t1.root, data)) else "Not found","in the tree")
    elif(c=="i"):
        data = int(input("Enter an element to insert into the BST:"))
        t1.root=t1.insert_node(t1.root,data)
        print("After inserction:",end=" ")
        t1.print_tree(t1.root)
    elif(c=="d"):
        data = int(input("Enter an element to delete from the BST:"))
        t1.root=t1.delete_node(t1.root,data)
        print("After delection:",end=" ")
        t1.print_tree(t1.root)
    elif(c=="m"):
        print("Minimum value in the tree is:", t1.FindMin())
    elif(c=="M"):
        print("Maximum value in the tree is:", t1.FindMax())
    elif(c=="p"):
        print("BST:",end=" ")
        t1.print_tree(t1.root)
    elif(c=="x"):
        break
    elif(c=="show"):
        show_choices()
    else:
        print("Invalid Input")
    
