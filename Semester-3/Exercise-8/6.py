# 6. Add a method delete(x, k) that deletes the node containing the key k 
# from the subtree rooted at the node x and returns the changed tree. 

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
    def print_inorder(self,temp):
        if temp:
            self.print_inorder(temp.left)
            print(temp.data,end=" ")
            self.print_inorder(temp.right)
t1=BST()
print("\n------------------------")
print("\n'i'-Insert node\n'd'-Delete node\n'p'-Print tree in inorder\n'x'-Exit")
print("\n------------------------\n")
while(1):
    c=input("\nEnter your choice(i/d/p/x):")
    if(c=="i"):
        data = int(input("Enter an element to insert into the BST:"))
        t1.root=t1.insert_node(t1.root,data)
    elif(c=="d"):
        data = int(input("Enter an element to delete from the BST:"))
        t1.root=t1.delete_node(t1.root,data)
        print("After delection:",end=" ")
        t1.print_inorder(t1.root)
    elif(c=="p"):
        print("Inoder traversal of BST:",end=" ")
        t1.print_inorder(t1.root)
    elif(c=="x"):
        break
    else:
        print("Invalid Input")