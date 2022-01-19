# 1. Develop a python program for implementing a Binary search tree. Perform the following
# operations:

# i. Insert() – Insert an element into the binary search tree
# ii. Delete a node which has 2 child, 1 child and no child
# iii. Level Traversal – Traverse the Binary Search Tree by level order.

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BST_Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        newnode = Node(data)
        temp = self.root
        if self.root is None:
            self.root = newnode
        else:
            temp = self.root
            while(1):
                if(temp.data >= data):
                    if(temp.left is None):
                        temp.left = newnode
                        break
                    temp = temp.left
                elif(temp.data < data):
                    if(temp.right is None):
                        temp.right = newnode
                        break
                    temp = temp.right

    def delete_node(self, current, data):
        if(current is None):
            return current
        elif(current.data > data):
            current.left = self.delete_node(current.left, data)
        elif(current.data < data):
            current.right = self.delete_node(current.right, data)
        else:
            if(current.left is None):
                temp = current.right
                current = None
                return temp
            elif(current.right is None):
                temp = current.left
                current = None
                return temp
            temp = current.right
            while(temp.left is not None):
                temp = temp.left
            current.data = temp.data
            current.right = self.delete_node(current.right, temp.data)
        return current
    def level_traversal(self, temp):
        if(temp == None):
            print("No elements in the Tree")
        else:
            q = []
            q.append(temp)
            print(temp.data, end=" ")
            while(len(q)):
                temp = q[0]
                q.pop(0)
                if(temp.left is not None):
                    print(temp.left.data, end=" ")
                    q.append(temp.left)
                if(temp.right is not None):
                    print(temp.right.data, end=" ")
                    q.append(temp.right)
t1 = BST_Tree()
while(1):
    print("\n----------------------\n")
    print("1.Insert node\n2.Delete node\n3.Level traversal\n4.Exit")
    print("\n----------------------\n")
    c = input("Enter your choice(1/2/3/4):")
    if(c == "1"):
        data = int(input("Enter an element to insert into BS-tree:"))
        t1.insert_node(data)
    elif(c == "2"):
        data = int(input("Enter an element to delete fron the BS-tree:"))
        t1.root=t1.delete_node(t1.root,data)
    elif(c == "3"):
        print("Level Traversal:", end=" ")
        t1.level_traversal(t1.root)
    elif(c == "4"):
        break
    else:
        print("Invalid input")
