# 1.
# Define a class Node to represent the nodes of a Binary Search Tree (BST).
# Node has 3 three fields:key,l, and r. Define two suitable constructors:
# Node(k) that takes only the key as a parameter,
# Node(k,l,r) that takes the key, left child, right child as parameters.
# Define a class BST.It has a Node field root.Define a method sample to create a sample BST.


class Node:
    def __init__(self, key, lchild=None, rchild=None):
        self.lchild = lchild
        self.key = key
        self.rchild = rchild
class BST:
    def __init__(self):
        self.root = None
    def insert_node(self, temp, data,lchild=None,rchild=None):
        if temp is None:
            return Node(data,lchild,rchild)
        elif temp.key > data:
            temp.lchild = self.insert_node(temp.lchild, data,lchild,rchild)
        else:
            temp.rchild = self.insert_node(temp.rchild, data,lchild,rchild)
        return temp
    def print_tree(self, temp):
        if temp:
            self.print_tree(temp.lchild)
            print(temp.key,end=" ")
            self.print_tree(temp.rchild)
def sample(c):
    if c=="ilr":
        print("*Before entering value for left-child,right-child of parent node.*")
        print("Check parent-data,left-child-data,right-child-data with BST values:")
        print("\t1.'left child-data'-It should be less than only its parent data")
        print("\t2.'right child-data'-It should be greater than only its parent data")
        print("BST-inorder-values:",end="")
        t1.print_tree(t1.root)
        data=int(input("\nEnter parent node data:"))  
        ldata=int(input("Enter left-child data:"))  
        rdata=int(input("Enter right-child data:"))
        lchild=Node(ldata)
        rchild=Node(rdata)
        t1.root=t1.insert_node(t1.root,data,lchild,rchild)
        print("After inserction:",end=" ")
        t1.print_tree(t1.root)
    elif c=="i":
        data = int(input("Enter an element to insert into the BST:"))
        t1.root=t1.insert_node(t1.root,data)
        print("After inserction:",end=" ")
        t1.print_tree(t1.root)
    elif c=="p":
        print("BST:",end=" ")
        t1.print_tree(t1.root)
print("\nOperations:")
print("----------------------------\n")
print("'i'-Insert an element into the tree")
print("'ilr'-insert parent,left-child-child into tree")
print("'p'-Print the BST")
print("'x'-Exits the program")
print("\n----------------------------\n")
t1=BST()
while(1):
    c = input("\nEnter your choice(i/ilr/p/x):")
    if(c=="x"):
        break
    elif(c=="i" or c=="ilr" or c=="p"):
        sample(c)
    else:
        print("Invalid Input")




        
