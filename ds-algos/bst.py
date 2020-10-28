# Simple Node class
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left

    def printVal(self):
        print(self.value)

    # Insert data into the BST using BST property and recursion
    def insert(self, value):
        if (value is not None):
            if value == self.value:
                self.value = value
            # Left side (smaller than node)
            if value < self.value:
                if self.left is None:
                    self.left = Node(value, None, None)
                else:
                    self.left.insert(value)
            # Right side (greater than node)
            else:
                if self.right is None:
                    self.right = Node(value, None, None)
                else:
                    self.right.insert(value)

# Left to root to right
def inOrderTraversal(node):
    if not node:
        return
    inOrderTraversal(node.left)
    node.printVal()
    inOrderTraversal(node.right)

# Root is visited first
def preOrderTraversal(node):
    if not node:
        return
    node.printVal()
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

# Root is visited last
def postOrderTraversal(node):
    if not node:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    node.printVal()

# Returns the node if it exists in the BST
def find(node, value):
    if (node is None or node.value == value):
        return node
        
    if value < node.value:
        return find(node.left, value)
    else:
        return find(node.right, value)

# Create a BST...
#
#           5
#         /   \
#        3    10
#       / \   / \
#      1   4 7  20
#
head = Node(5, None, None)
values = [3,10,1,4,7,20]
for i in values:
    head.insert(i)


print(find(head, 42))