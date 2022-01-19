# 3.Binary tree

#       14
#     /    \
#    2      11
#   /  \   /  \
# 1    3  10   30
#     /          \
#    7            40

# write the program to find the order of the nodes.
# (i). An in-order traversal
# (ii). A pre-order traversal
# (iii). A post-order traversal

class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BT:
    def __init__(self):
        self.root = None

    def insert(temp, key):
        if not temp:
            root = Node(key)
            return
        q = []
        q.append(temp)
        while (len(q)):
            temp = q[0]
            q.pop(0)
            if (not temp.left):
                temp.left = Node(key)
                break
            else:
                q.append(temp.left)

            if (not temp.right):
                temp.right = Node(key)
                break
            else:
                q.append(temp.right)

    def in_order(self, temp):
        if(temp is None):
            return
        self.in_order(temp.left)
        print(temp.data, end=" ")
        self.in_order(temp.right)

    def pre_order(self, temp):
        if(temp is None):
            return
        print(temp.data, end=" ")
        self.pre_order(temp.left)
        self.pre_order(temp.right)

    def post_order(self, temp):
        if(temp is None):
            return
        self.post_order(temp.left)
        self.post_order(temp.right)
        print(temp.data, end=" ")


if __name__ == '__main__':
    t1 = BT()
    t1.root = Node(14)
    t1.root.left = Node(2)
    t1.root.right = Node(11)
    t1.root.left.left = Node(1)
    t1.root.left.right = Node(3)
    t1.root.right.left = Node(10)
    t1.root.right.right = Node(30)
    t1.root.left.right.left = Node(7)
    t1.root.right.right.right = Node(40)
    print("In-Order:", end=" ")
    t1.in_order(t1.root)
    print("\nPre-Order:", end=" ")
    t1.pre_order(t1.root)
    print("\nPost-Order:", end="")
    t1.post_order(t1.root)
