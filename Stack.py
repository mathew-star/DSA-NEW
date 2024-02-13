"""
->empty()  Returns whether the stack is empty>>>  Time Complexity: O(1)

->size()  Returns the size of the stack>>  Time Complexity: O(1)

->top() / peek()  Returns a reference to the topmost element of the stack>> Time Complexity: O(1)

->push(a)  Inserts the element ‘a’ at the top of the stack >>> Time Complexity: O(1)

->pop()  Deletes the topmost element of the stack >>Time Complexity: O(1)
Stack in Python can be implemented using the following ways: 

list
Collections.deque
queue.LifoQueue

Python stack can be implemented using the deque class from the collections module.
Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container,
as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 

"""
# Python program to
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty



# Python program to
# demonstrate stack implementation
# using collections.deque

from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty




# Python program to
# demonstrate stack implementation
# using queue module

from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())





#Stack in linked list>>
# python3 program to Implement a stack
# using singly linked list

class Node:

	# Class to create nodes of linked list
	# constructor initializes node automatically
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:

	# head is default NULL
	def __init__(self):
		self.head = None

	# Checks if stack is empty
	def isempty(self):
		if self.head == None:
			return True
		else:
			return False

	# Method to add data to the stack
	# adds to the start of the stack
	def push(self, data):

		if self.head == None:
			self.head = Node(data)

		else:
			newnode = Node(data)
			newnode.next = self.head
			self.head = newnode

	# Remove element that is the current head (start of the stack)
	def pop(self):

		if self.isempty():
			return None

		else:
			# Removes the head node and makes
			# the preceding one the new head
			poppednode = self.head
			self.head = self.head.next
			poppednode.next = None
			return poppednode.data

	# Returns the head node data
	def peek(self):

		if self.isempty():
			return None

		else:
			return self.head.data

	# Prints out the stack
	def display(self):

		iternode = self.head
		if self.isempty():
			print("Stack Underflow")

		else:

			while(iternode != None):

				print(iternode.data, end = "")
				iternode = iternode.next
				if(iternode != None):
					print(" -> ", end = "")
			return


# Driver code
if __name__ == "__main__":
MyStack = Stack()

MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)

# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is ", MyStack.peek())

# Delete top elements of stack
MyStack.pop()
MyStack.pop()

# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is ", MyStack.peek())




## Implementation of stack using queue>>
q=deque()
def push(val):
	n=len(q)
	q.append(val)
	for _ in range(n):
		q.append(q.popleft())
def pop():
	return q.popleft()
print("###########")
push(10)
push(20)
push(30)
print(q)
print("###########")
print(q.pop())
