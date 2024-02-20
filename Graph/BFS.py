from collections import defaultdict,deque
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add_edge(self, v1,v2):
        self.graph[v1].append(v2)
        
    def bsf(self,v):
        visited=set()
        queue=deque([v])
        while queue:
                current=queue.popleft()
                if current not in visited:
                    print(current, end=" ")
                    visited.add(current)
                    queue.extend(self.graph[current])


g=graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.bsf(1)

