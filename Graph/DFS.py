from collections import defaultdict,deque
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add_edge(self, v1,v2):
        self.graph[v1].append(v2)

    def dsf(self,v,visited=None):
        if visited is None:
            visited=set()
        visited.add(v)
        print(v,end=" ")
        for n in self.graph[v]:
            if n not in visited:
                self.dsf(n,visited)

                    

g=graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.dsf(1)

