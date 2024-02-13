# Python3 program to for tree traversals


# A class that represents an individual node in a
# Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# Then print the data of node
		print(root.val, end=" "),

		# Now recur on right child
		printInorder(root.right)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Inorder traversal of binary tree is")
	printInorder(root)
"""
Inorder traversal of binary tree is 
4 2 5 1 3 
"""



# Python3 program to for tree traversals


# A class that represents an individual node
# in a Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do preorder tree traversal
def printPreorder(root):

	if root:

		# First print the data of node
		print(root.val, end=" "),

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Preorder traversal of binary tree is")
	printPreorder(root)
"""
Preorder traversal of binary tree is 
1 2 4 5 3  
    """



# Python3 program to for tree traversals
#Post-Order
# A class that represents an individual node
# in a Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do postorder tree traversal
def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# The recur on right child
		printPostorder(root.right)

		# Now print the data of node
		print(root.val, end=" "),


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Postorder traversal of binary tree is")
	printPostorder(root)
