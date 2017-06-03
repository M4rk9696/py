# Ford-Fulkerson for finding max flow
# Max flow is found by using max-flow-min-cut-theorm
# Wikipedia implementation keeping in my repo for my reference all credits to orginal author of implementation
import collections
 
class Graph:
  def __init__(self, graph):
    self.graph = graph # residual graph
    self. ROW = len(graph)
  
  def BFS(self,s, t, parent):
    visited = [False] * (self.ROW)
    queue = collections.deque()
         
    queue.append(s)
    visited[s] = True
         
    while queue:
      u = queue.popleft()

      for ind, val in enumerate(self.graph[u]):
        if visited[ind] == False and val > 0 :
          queue.append(ind)
          visited[ind] = True
          parent[ind] = u
 
    return visited[t]
             
  def FordFulkerson(self, source, sink):
    parent = [-1] * (self.ROW)
    max_flow = 0
 
    while self.BFS(source, sink, parent) :
      path_flow = float("Inf")
      s = sink
      while s !=  source:
        path_flow = min (path_flow, self.graph[parent[s]][s])
        s = parent[s]
        max_flow +=  path_flow
        v = sink
        while v !=  source:
          u = parent[v]
          self.graph[u][v] -= path_flow
          self.graph[v][u] += path_flow
          v = parent[v]
 
    return max_flow

g = Graph([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]])
print g.FordFulkerson(0, 3)
