class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if (head is None):
            return False
        
        tort = head
        hare = head.next
        
        while (hare != tort):
            if (hare is None or hare.next is None):
                return False
            else:
                hare = hare.next.next
                tort = tort.next
                
        return True