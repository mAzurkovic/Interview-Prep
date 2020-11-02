class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if (len(self.queue) == 0):
            return True
        else:
            return False

    def peek(self):
        return self.queue[-1]

    def add(self, value):
        self.queue.append(value)

    def dequeue(self):
        if (self.queue is not None):
            self.queue = self.queue[1:]
        else:
            return -1

    def printQueue(self):
        for i in range(0, len(self.queue)):
            print(self.queue[i])

    

q = Queue()

print(q.printQueue())