class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

# Wrapper class that holds Linked List functions
class LinkedList:
    def __init__(self, head):
        self.head = head

    # Append a single item
    def append(self, value):
        current = self.head
        while True:
            if (current.next == None):
                end = Node(value, None)
                current.next = end
                break
            else:
                current = current.next

    # Add values from a list
    def appendList(self, values):
        for value in values:
            self.append(value)

    # Print values in the linked list
    def printList(self):
        current = self.head

        while True:
            print(current.value)
            if (current.next == None):
                break
            else:
                current = current.next

head = Node(5, None)

ll = LinkedList(head)
ll.appendList([10,20,20])
ll.printList()

    
