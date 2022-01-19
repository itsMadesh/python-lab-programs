class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def addEdge(self, u, v):
        try:
            self.graph[u]
        except:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def isCyclic(self):
        parent = [-1] * (self.V)
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


g1 = Graph(4)
print("OUTPUT 1")
g1.addEdge(0, 1)
g1.addEdge(3, 2)
g1.addEdge(2, 0)
print("The given graph: ", g1.graph)
if g1.isCyclic():
    print("The graph is cyclic")
else:
    print("The graph is non-cyclic")
g2 = Graph(4)
print("OUTPUT 2")
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
print("The given graph: ", g2.graph)
if g2.isCyclic():
    print("The graph is cyclic")
else:
    print("The graph is non-cyclic")
