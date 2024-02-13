

from collections import deque
## Implementation of stack using queue>>
q=[]
def push(val):
	n=len(q)
	q.append(val)
	for _ in range(n):
		q.append(q[0])
		del q[0]
def pop():
	return q[0]
def top():
	return q[-1]
print("###########")
push(10)
push(20)
push(30)
print("###########")
print(pop())
print(top())

#Implementation of queue using two stacks>>

s1=[]
s2=[]

def enqueue(v):
	while len(s1) != 0:
		s2.append(s1.pop())
	s1.append(v)
	while len(s2) != 0:
		s1.append(s2.pop())

def dequeue():
	return s1.pop()

print("#########")
enqueue(1)
enqueue(12)
enqueue(13)
print(s1)

print(dequeue())


