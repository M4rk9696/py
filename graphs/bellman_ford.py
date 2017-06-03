# Assuming the graph is an adjacency matrix
def bellman_ford(grph, src, dest):
  inf = 999999999 # Can be replaced by float("Inf")
  n = len(grph)
  dist = [inf] * n
  pred = [None] * n

  dist[src] = 0

  # Path relaxation
  for i in range(n):
    for u in range(n):
      for v in range(n):
        w = grph[u][v]
        if dist[u] + w < dist[v]:
          dist[v] = dist[u] + w
          pred[v] = u

  # Negative cycle detection
  for u in range(n):
    for v in range(n):
      w = grph[u][v]
      if dist[u] + w < dist[v]:
        return -1

  return dist, pred

print bellman_ford([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]], 0, 3)
