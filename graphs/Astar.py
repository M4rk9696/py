import heapq

class PriorityQueue:
	def __init__(self):
		self.elements = []

	def empty(self):
		return len(self.elements) == 0

	def put(self, item, priority):
		heapq.heappush(self.elements, (priority, item))

	def get(self):
		return heapq.heappop(self.elements)[1]

class Graph:
	def __init__(self):
		self.WEdges = {}
		self.weight = {}

	def Nodeweight(self, node):
		return self.weight[node]
		
	def neighbors(self, node):
		if node in self.WEdges:
			return self.WEdges[node].keys()
		else:
			return {}

	def cost(self, node, to):
		return self.WEdges[node][to]

def hfunction(pta, ptb):
	(x1, y1) = pta
	(x2, y2) = ptb
	return abs(x1 - x2) + abs(y1 - y2)

def a_star(graph, start, goal):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	cost = {}

	came_from[start] = None
	cost[start] = graph.Nodeweight(start)

	while not frontier.empty():
		current = frontier.get()

		if current == goal:
			break

		for next in graph.neighbors(current):
			new_cost = cost[current] + graph.cost(current, next)
			if next not in cost or new_cost < cost[next]:
				cost[next] = new_cost
				priority = new_cost + hfunction(goal, next)
				frontier.put(next, priority)
				came_from[next] = current
	return cost

def main():
	inf = 100000000
	fname = 'p083_matrix.txt'
	with open(fname) as f:
		content = f.readlines()
	content = [x.strip().split(',') for x in content]
	n = len(content)
	content = [[inf] * (n + 2)] + [[inf] + [int(a) for a in x] + [inf] for x in content] + [[inf] * (n + 2)]
	n = len(content)

	graph = Graph()

	for i in range(1, n-1):
		for j in range(1, n-1):
			pos = (i, j)
			graph.weight[pos] = content[i][j]
			## top
			ii, jj = i - 1, j
			node = (ii, jj)
			weight = content[ii][jj]
			graph.WEdges[pos] = {}
			graph.WEdges[pos][node] = weight

			## botton
			ii, jj = i + 1, j
			node = (ii, jj)
			weight = content[ii][jj]
			graph.WEdges[pos][node] = weight

			## left
			ii, jj = i, j - 1
			node = (ii, jj)
			weight = content[ii][jj]
			graph.WEdges[pos][node] = weight

			## right
			ii, jj = i, j + 1
			node = (ii, jj)
			weight = content[ii][jj]
			graph.WEdges[pos][node] = weight
			
	# print graph.WEdges
	# print graph.neighbors((5, 5))
	# print graph.cost((1, 1), (1, 2))
	st = (1, 1)
	en = (n - 2, n - 2)
	print a_star(graph, st, en)[en]
	# print content

main()