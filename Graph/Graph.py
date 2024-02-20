
#undirected   
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1) 

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {', '.join(map(str, self.graph[vertex]))}")

# Example Usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.display()


#Adjecent matrix
class graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[0]*vertices for _ in range(vertices)]
        
    def add_edge(self,vertx1, vertx2):
        self.graph[vertx1][vertx2]= 1
        self.graph[vertx2][vertx1]=1
        
    def display(self):
        for row in self.graph:
            print(' '.join(map(str, row)))


g = graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.display()            


#weighted undirected  graph
from collections import defaultdict

class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v1, v2, weight):
        self.graph[v1].append((v2, weight))
        self.graph[v2].append((v1, weight)) 

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

wg = WeightedGraph()
wg.add_edge(1, 2, 3)
wg.add_edge(1, 3, 2)
wg.add_edge(2, 4, 5)
wg.add_edge(3, 4, 1)

wg.print_graph()


#WeightedDirectedGraph
from collections import defaultdict

class WeightedDirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, source, destination, weight):
        self.graph[source].append((destination, weight))

    def display_graph(self):
        for vertex in self.graph:
            print(f"Vertex {vertex}: ", end="")
            for edge, weight in self.graph[vertex]:
                print(f"({edge}, {weight})", end=" ")
            print()


g = WeightedDirectedGraph()
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 4)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 1)

g.display_graph()


"""

The main difference between the code for a directed graph and an undirected graph lies in how edges are
added. In an undirected graph,if there is an edge from vertex A to vertex B, there is also an edge 
from B to A. In a directed graph,edges have a specific direction, going from one vertex to another
"""
class UndirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # Add the reverse edge

    def display_graph(self):
        for vertex in self.graph:
            print(f"Vertex {vertex}: {self.graph[vertex]}")

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, source, destination):
        self.graph[source].append(destination)

    def display_graph(self):
        for vertex in self.graph:
            print(f"Vertex {vertex}: {self.graph[vertex]}")
