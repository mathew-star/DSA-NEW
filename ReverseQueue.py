
from collections import deque
q=deque()
def reverse():
    s=[]
    while q:
        s.append(q.popleft())
    while len(s)!=0:
        q.append(s.pop())
q.append(1)
q.append(12)
q.append(13)
q.append(14)
print("Original Que: ",q)
reverse()
print("Reversed Que: ",q)

for i in q:
    print(i, end=" ")