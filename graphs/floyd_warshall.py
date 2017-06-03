# All path shortest path
# Assuming in adjacency matrix
import copy

def floyd(grph):
  n = len(grph)
  dist = copy.deepcopy(grph)

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

  return dist

print floyd([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]])  
