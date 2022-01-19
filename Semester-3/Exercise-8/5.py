# 5. Add two methods findMin (x) to the Bst class. It should return the node containing the 
# smallest key in the subtree rooted at the node x. 
# Add a method deleteMin(x) to the Bst class that deletes the node containing the smallest key in the 
# tree rooted at the node x, and returns the updated tree. 


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
    def find_min(self):
        temp = self.root
        if temp is None:
            return temp
        else:
            while temp.left is not None:
                temp = temp.left
            return temp.data
    def delete_min(self,current):
        if(current.left is None):
            return current.right
        else:
            current.left=self.delete_min(current.left)
        return current
    def print_inorder(self,temp):
        if temp:
            self.print_inorder(temp.left)
            print(temp.data,end=" ")
            self.print_inorder(temp.right)
t1=BST()
print("\n------------------------")
print("\n'i'-Insert node\n'm'-Find minimum value\n'dm'-Delete minimum value\n'p'-Print tree in inorder\n'x'-Exit")
print("\n------------------------\n")
while(1):
    c=input("\nEnter your choice(i/m/dm/p/x):")
    if(c=="i"):
        data = int(input("Enter an element to insert into the BST:"))
        t1.root=t1.insert_node(t1.root,data)
    elif(c=="d"):
        data = int(input("Enter an element to delete from the BST:"))
        t1.root=t1.delete_node(t1.root,data)
        print("After delection:",end=" ")
        t1.print_inorder(t1.root)
    elif(c=="m"):
        print("Minimum value in the tree is:", t1.find_min())
    elif(c=="dm"):
        t1.root=t1.delete_min(t1.root)
        print("After delection of minimum value:",end=" ")
        t1.print_inorder(t1.root)
    elif(c=="p"):
        print("Inoder traversal of BST:",end=" ")
        t1.print_inorder(t1.root)
    elif(c=="x"):
        break
    else:
        print("Invalid Input")