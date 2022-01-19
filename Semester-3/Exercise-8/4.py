# 4. Add a method Node insert (x, k) to the Bst class. It inserts the key k in the 
# subtree rooted at the node x of the BST, and returns the changed tree. 


class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
class BST:
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
    def print_inorder(self,temp):
        if temp:
            self.print_inorder(temp.left)
            print(temp.data,end=" ")
            self.print_inorder(temp.right)
t1=BST()
print("\n------------------------")
print("\n'i'-Insert node\n'p'-Print tree in inorder\n'x'-Exit")
print("\n------------------------\n")
while(1):
    c=input("\nEnter your choice(i/p/x):")
    if(c=="i"):
        data = int(input("Enter an element to insert into the BST:"))
        t1.root=t1.insert_node(t1.root,data)
    elif(c=="p"):
        print("Inoder traversal of BST:",end=" ")
        t1.print_inorder(t1.root)
    elif(c=="x"):
        break
    else:
        print("Invalid Input")