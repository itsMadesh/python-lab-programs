# 2. Create a Binary search tree for the following list.
# 30, 20, 25, 22, 40, 42, 35, 37
# Perform the following operations:
# i. FindMin()
# ii. Search() – Search a random element
# iii. FindMax()
# iv. Empty()

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BST_Tree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
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

    def search(self, temp, data):
        if(temp == None or temp.data == data):
            return temp
        elif(temp.data > data):
            return self.search(temp.left, data)
        else:
            self.search(temp.right, data)

    def FindMin(self):
        temp = self.root
        if temp is None:
            return "No elements in the tree"
        else:
            while(temp.left is not None):
                temp = temp.left
            return temp.data

    def FindMax(self):
        temp = self.root
        if temp is None:
            return "No elements in the tree"
        else:
            while(temp.right is not None):
                temp = temp.right
            return temp.data

    def display(self, temp):
        if(temp is None):
            return -1
        print(temp.data)
        self.display(temp.left)
        self.display(temp.right)

    def empty(self):
        return self.root == None


a = [30, 20, 25, 22, 40, 42, 35, 37]
t1 = BST_Tree()
for i in a:
    t1.add_node(i)
print("Minimum value in the tree is:", t1.FindMin())
print("Maximum value in the tree is:", t1.FindMax())
print("Search value-5 in tree:",
      "Found" if (t1.search(t1.root, 5)) else "Not found")
print("Search value-30 in tree:",
      "Found" if (t1.search(t1.root, 30)) else "Not found")
print("Tree is empty:",t1.empty())
