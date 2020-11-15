import collections

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = deque()
        while (head is not None):
            stack.append(head.val)
            head = head.next
            
        print(stack)
        head = ListNode(0)
        current = head
        for i in range(len(stack)):
            node = ListNode(stack.pop())
            current.next = node
            current = current.next 
            
        return head.next