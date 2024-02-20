
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
Case 1: (0—n-1) 
--------------
if (say)father=p; 
then left_son=(2*p)+1; 
and right_son=(2*p)+2;

Case 2: 1—n
-----------
if (say)father=p; 
then left_son=(2*p); 
and right_son=(2*p)+1; 
"""
# Python3 implementation of tree using array
# numbering starting from 0 to n-1.
tree = [None] * 10
 
 
def root(key):
    if tree[0] != None:
        print("Tree already had root")
    else:
        tree[0] = key
 
 
def set_left(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 1, ", no parent found")
    else:
        tree[(parent * 2) + 1] = key
 
 
def set_right(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 2, ", no parent found")
    else:
        tree[(parent * 2) + 2] = key
 
 
def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()
 
 
# Driver Code
root('A')
set_left('B', 0)
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()
 