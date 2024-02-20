# Python program to find the height of 
# an N-ary tree 

# Structure of a node of an n-ary tree 
class Node: 
	def __init__(self, key): 
		self.key = key 
		self.child = [] 

# Utility function to create a new tree node 
def new_node(key): 
	temp = Node(key) 
	return temp 

# Function that will return the depth 
# of the tree 
def depth_of_tree(ptr): 
	# Base case 
	if ptr is None: 
		return 0

	# Check for all children and find 
	# the maximum depth 
	maxdepth = 0
	for child in ptr.child: 
		maxdepth = max(maxdepth, depth_of_tree(child)) 

	return maxdepth + 1

# Driver program 
if __name__ == '__main__': 
	""" Let us create below tree 
			A 
		/ / \ \ 
		B F D E 
		/ \ | /|\ 
		K J G C H I 
		/\		 \ 
		N M		 L 
	"""

	root = new_node('A') 
	root.child.extend([new_node('B'), new_node('F'), new_node('D'), new_node('E')]) 
	root.child[0].child.extend([new_node('K'), new_node('J')]) 
	root.child[2].child.append(new_node('G')) 
	root.child[3].child.extend([new_node('C'), new_node('H'), new_node('I')]) 
	root.child[0].child[0].child.extend([new_node('N'), new_node('M')]) 
	root.child[3].child[2].child.append(new_node('L')) 

	print(depth_of_tree(root)) 



#Another Simple implementation >>
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class NaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data, parent=None):
        node = TreeNode(data)
        if not parent:
            self.root = node
        else:
            parent.children.append(node)

    def preorder_traversal(self, node):
        result = [node.data]
        for child in node.children:
            result += self.preorder_traversal(child)
        return result

    def preorder(self):
        if not self.root:
            return []
        return self.preorder_traversal(self.root)

if __name__ == "__main__":
    nary_tree = NaryTree()

    nary_tree.insert(1)
    nary_tree.insert(2, nary_tree.root)
    nary_tree.insert(3, nary_tree.root)
    nary_tree.insert(4, nary_tree.root.children[0])
    nary_tree.insert(5, nary_tree.root.children[0])
    nary_tree.insert(6, nary_tree.root.children[1])

    print("Preorder Traversal:", nary_tree.preorder())
