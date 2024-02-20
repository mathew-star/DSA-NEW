class Node:
    def __init__(self, data):
        self.data = data
        self.left=self.right=None

def Insert(node,val):
    if node is None:
        return Node(val)
    else:
        if val<node.data:
            node.left=Insert(node.left,val)
        elif val>node.data:
            node.right=Insert(node.right,val)
    return node
def dfs(node,key):
    if node==None:
        return False
    if node.data == key:
        return True
    return dfs(node.left,key) or dfs(node.right,key)

def breathFirstSearch(root,key):
    if root is None:
        return False
    q=[]
    q.append(root)
    while q:
        node=q[0]
        del q[0]
        if node.data==key:
            return True
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return False
            


# Function to print leaf nodes
# from left to right
def printLeafNodes(root):
    # If node is null, return
    if not root:
        return
 
    # If node is leaf node,
    # print its data
    if not root.left and not root.right:
        print(root.key, end=" ")
 
    # If left child exists,
    # check for leaf recursively
    if root.left:
        printLeafNodes(root.left)
 
    # If right child exists,
    # check for leaf recursively
    if root.right:
        printLeafNodes(root.right)





# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.key, end=' ')
    elif level > 1:
        # Recursive Call
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

r=None
r=Insert(r,50)
Insert(r,30)
Insert(r,40)

inorder(r)

key=30
if breathFirstSearch(r,key):
    print("")
    print(key,"found")
else:
    print(key,"No")
"""Time Complexity: O(N), where N is the number of nodes of the BST 
Auxiliary Space: O(1) 

Inorder traversal: In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order.
We visit the left child first, then the root, and then the right child.
    """
    
