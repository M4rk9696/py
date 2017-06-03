# Kruskal for minimum spanning tree
# Assuming input is adjacency list

class Graph:
  def __init__(self):
    self.arr = []

  def initialise(self, n):
    self.arr = range(n)

  def root(self, x):
    if x != self.arr[x]:
      self.arr[x] = self.root(self.arr[x])
    return self.arr[x]

  def union(self, x, y):
    self.arr[self.root(y)] = self.root(x)

  def kruskal(self, grph, n):
    new_graph = [[] for _ in range(n)]
    self.initialise(n)
    
    for node, vertex in enumerate(grph):
      for neighbour in vertex:
        if self.root(node) != self.root(neighbour):
          new_graph[node].append(neighbour)
          new_graph[neighbour].append(node)
        
          self.union(node, neighbour)
    return new_graph

g = Graph()
n = 5
print g.kruskal([range(n) for _ in range(n)], n)
