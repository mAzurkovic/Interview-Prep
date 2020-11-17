class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def printValue(self):
        print(self.value)

node = Node(10)

node.printValue()