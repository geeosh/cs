#!/usr/bin/python
# Depth-First Search

from data_structures.graph import Graph
from data_structures.graph import EdgeNode

from collections import deque

class DFS:
  
  def __init__(self, graph):
    self.graph = graph
    self.processed = [False for x in range(self.graph.max_vertices)]
    self.discovered = [False for x in range(self.graph.max_vertices)]
    self.entry_time = [0 for x in range(self.graph.max_vertices)]
    self.exit_time = [0 for x in range(self.graph.max_vertices)]
    self.parent = [-1 for x in range(self.graph.max_vertices)]
    self.time = 0

  def process_graph(self, vertex):
    finished = False

    self.discovered[vertex] = True
    self.time += 1
    self.entry_time[vertex] = self.time

    self.process_vertex_early(vertex)

    node = self.graph.edges[vertex]

    while(node != None):
      y = node.y
      if(self.discovered[y] == False):
        self.parent[y] = vertex
        self.process_edge(vertex,y)
        self.process_graph(y)
      elif(not self.processed[y] or self.graph.directed):
        self.process_edge(vertex,y)
      
      if(finished):
        return
        
      node = node.next

    self.process_vertex_late(vertex)
    self.time += 1
    self.exit_time[vertex] = self.time
    self.processed[vertex] = True


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

print "\nInitialize DFS and process graph"

dfs = DFS(graph)
dfs.process_graph(1)

print "\nFind shortest path from 1 to 20:"
print " - ".join(str(i) for i in dfs.find_path(1,20))