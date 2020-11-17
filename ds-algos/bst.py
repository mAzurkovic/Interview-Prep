from collections import deque

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



# This is DFS on a binary tree using a stack DS rather than recursion
def dfsStack(node, target):
    seen = set() 
    stack = deque()
    stack.append(node)

    while (len(stack) != 0):
        # Set the current proccesing node to the top of the stack (.pop())
        current = stack.pop()

        # If not seen, proccess it
        if (current not in seen):
            if (current.value == target):
                return current
            # Add it to the hashset
            seen.add(current)
        
        # Check the children, if not binary tree and n-ary tree, iterate through dynamically
        # Make sure its not null and not seen before
        if (current.left is not None and current.left not in seen):
            stack.append(current.left)
        if (current.right is not None and current.left not in seen):
            stack.append(current.right)
    
    return -1


seen = set()
def dfs(node, target):
    if (node is not None and node not in seen):
        if (node.value == target):
            return node
        seen.add(node)
        dfs(node.left, target)
        dfs(node.right, target)
    else:
        return -1  

# This is BFS on a binary tree
def bfsStack(node, target):
    seen = set() 
    queue = deque()
    queue.append(node)

    while (len(queue) != 0):
        # Set the current proccesing node, dequeue the data structure
        current = queue.popleft()

        # If not seen, proccess it
        if (current not in seen):
            if (current.value == target):
                return current
            # Add it to the hashset
            seen.add(current)
        
        # Check the children, if not binary tree and n-ary tree, iterate through dynamically
        # Make sure its not null and not seen before
        if (current.left is not None and current.left not in seen):
            queue.append(current.left)
        if (current.right is not None and current.left not in seen):
            queue.append(current.right)
    
    return -1


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

print(bfsStack(head, 10))