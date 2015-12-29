#!/usr/bin/python
# Breadth-First Search, useful for discovering shortest path

from data_structures.graph import Graph
from data_structures.graph import EdgeNode

from collections import deque

class BFS:
  
  def __init__(self, graph):
    self.graph = graph
    self.processed = [False for x in range(self.graph.max_vertices)]
    self.discovered = [False for x in range(self.graph.max_vertices)]
    self.parent = [-1 for x in range(self.graph.max_vertices)]

  def process_graph(self, start):
    queue = deque()
    vertex, y = None, None

    queue.append(start)
    self.discovered[start] = True

    while(len(queue) > 0):
      vertex = queue.popleft()
      self.process_vertex_early(vertex)
      self.processed[vertex] = True
      node = self.graph.edges[vertex]
      
      while(node != None):
        y = node.y
        if(self.processed[y] == False or self.graph.directed):
          self.process_edge(vertex,y)
        if(self.discovered[y] == False):
          queue.append(y)
          self.discovered[y] = True
          self.parent[y] = vertex
        node = node.next

      self.process_vertex_late(vertex)

  def process_vertex_early(self, vertex):
    print "Processed vertex %d" % vertex

  def process_vertex_late(self, vertex):
    return

  def process_edge(self, x, y):
    print "Processed edge (%d,%d)" % (x,y)

  def find_path(self, start, end):
    path = []

    if(start == end or end == -1):
      path.append(start)
    else:
      path += self.find_path(start, self.parent[end])
      path.append(end)

    return path


print "Initialize Graph:"

graph = Graph(1000, False)
graph.insert_edge(1, 2)
graph.insert_edge(1, 3)
graph.insert_edge(1, 4)
graph.insert_edge(10, 1)
graph.insert_edge(10, 2)
graph.insert_edge(20, 2)
graph.print_graph()

print "\nInitialize BFS and process graph"

bfs = BFS(graph)
bfs.process_graph(1)

print "\nFind shortest path from 1 to 20:"
print " - ".join(str(i) for i in bfs.find_path(1,20))