class Stack:
    # Use array ds as the base storage element
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if (len(self.stack) == 0):
            return True
        else:
            return False

    # Push to top of stack
    def push(self, value):
        self.stack.append(value)

    # Remove last intem in stack
    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def length(self):
        return len(self.stack)

    def printStack(self):
        for i in self.stack:
            print(i)

stack = Stack()
stack.push(1)
stack.push(10)
print(stack.peek())
print(stack.printStack())