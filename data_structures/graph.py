#!/usr/bin/python
# Adjacency List that is useful for storing graph structures
# Based on Skiena's design: https://www3.cs.stonybrook.edu/~skiena/392/programs/graph.c

class Graph:
  
  def __init__(self, max_vertices, directed = False):
    self.max_vertices = max_vertices
    self.directed = directed
    self.num_vertices = 0
    self.num_edges = 0

    # Initialize data structure to hold edges
    self.edges = [None for x in range(self.max_vertices)]

    # Initialize degree as 0 for all edge indices
    self.degree = [0 for x in range(self.max_vertices)]

  def insert_edge(self, x, y, directed = None):
    if(directed == None):
      directed = self.directed

    # Increment # of vertices if we haven't added an edge here yet
    self.num_vertices += 1

    # Create new node, pointing next to the current head
    edge = EdgeNode(y, None, self.edges[x])

    # Insert at head of the list
    self.edges[x] = edge
    self.degree[x] += 1

    if(not directed):
      self.insert_edge(y, x, True)
    else:
      self.num_edges += 1

  def delete_edge(self, x, y, directed = None):
    if(directed == None):
      directed = self.directed

    prev = None
    edge = self.edges[x]
    for i in range(self.degree[x]):
      # Found it!
      if(edge.y == y):
        # At head, so assign
        if(prev is None):
          self.edges[x] = edge.next
          if(self.edges[x] == None):
            self.num_vertices -= 1
        else:
          prev.next = edge.next
        
        self.degree[x] -= 1

        if(not directed):
          self.delete_edge(y,x,True)

        return

      prev = edge
      edge = edge.next

    print "Warning: deletion(%d,%d) not found in graph" % (x,y)

  def print_graph(self):
    for i in range(len(self.edges)):
      if(self.edges[i] != None):
        string = "%d:" % i
        p = self.edges[i]
        while(p != None):
          string += " %d" % p.y
          p = p.next
        print string

    
class EdgeNode:
  
  def __init__(self, y, weight = None, next_node = None):
    self.y = y
    self.weight = weight
    self.next = next_node


print "Initialize Graph with Adjacency List:"

graph = Graph(1000, False)
graph.insert_edge(1, 2)
graph.insert_edge(1, 3)
graph.insert_edge(1, 4)
graph.insert_edge(10, 1)
graph.insert_edge(10, 2)
graph.insert_edge(20, 2)
graph.print_graph()

print "\nRemove 1 -- 2"
graph.delete_edge(1,2)
print "Remove 1 -- 10"
graph.delete_edge(1,10)
print "\nNew graph:"
graph.print_graph()
