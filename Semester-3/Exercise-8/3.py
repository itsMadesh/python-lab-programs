# 3. Add a method Node search(x, k) to the Bst class. It searches the subtree rooted 
# at x for the key k and returns the node cotaining k. 
# If k is not found, it returns null. 

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
    def search(self, temp, data):
        if temp == None or temp.data == data:
            return temp
        elif temp.data > data:
            return self.search(temp.left, data)
        else:
            return self.search(temp.right, data)
t1=BST()
print("\n------------------------")
print("\n'i'-Insert node\n's'-Search key\n'x'-Exit")
print("\n------------------------\n")
while(1):
    c=input("\nEnter your choice(i/s/x):")
    if(c=="i"):
        data = int(input("Enter an element to insert into the BST:"))
        t1.root=t1.insert_node(t1.root,data)
    elif(c=="s"):
        data = int(input("Enter an element to search:"))
        print("Search key-{0} in the tree:".format(data),t1.search(t1.root,data))
    elif(c=="x"):
        break
    else:
        print("Invalid Input")

    