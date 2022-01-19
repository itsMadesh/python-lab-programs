# Write a Python program to create an expression tree and perform its inorder, preorder and
# postorder traversals.


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def expression_tree(exp):
    s = []
    for i in exp:
        # if(i.isdigit() or i.isalpha()):
        if i == "+" or i == "-" or i == "^" or i == "/" or i == "*":
            newnode = Node(i)
            newnode.right = s.pop()
            newnode.left = s.pop()
            s.append(newnode)
        else:
            newnode = Node(i)
            s.append(newnode)
    return s.pop()


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end="")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.key, end="")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end="")


exp = input("Enter postfix expression:")
root = expression_tree(exp)
print("Inorder traversal:", end="")
inorder(root)
print("\nPreorder traversal:", end="")
preorder(root)
print("\nPostorder traversal:", end="")
postorder(root)
