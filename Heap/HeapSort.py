def build(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        max_heapify_forSort(arr,i,n)
        
def heapsort(arr):
    build(arr)
    for i in range(len(arr)-1 ,0,-1):
        arr[i], arr[0] = arr[0] , arr[i]
        max_heapify_forSort(arr,0,i)




def max_heapify_forSort(arr,i,size):
    l=i
    left=2*i +1
    right= 2*i +2
    if left<size and arr[left] > arr[l]:
        l=left
    if right<size and arr[right] > arr[l]:
        l=right
    if l != i:
        arr[i],arr[l]=arr[l],arr[i]
        max_heapify_forSort(arr,l,size)
        
     

arr=[4,10,3,5,1]
print(arr)
heapsort(arr)
print("Sorted : ",arr)


from collections import defaultdict,deque
class graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    def add(self,v1,v2):
        self.graph[v1].append(v2)
    def bfs(self,v):
        visited = set()
        q=deque([v])
        while q:
            c=q.popleft()
            if c not in visited:
                print(c, end=" ")
                visited.add(c)
                q.extend(self.graph[c])

g=graph()
g.add(1,2)
g.add(1,3)
g.add(2,3)
g.add(2,4)
g.bfs(1)