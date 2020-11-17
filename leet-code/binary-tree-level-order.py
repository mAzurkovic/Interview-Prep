# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
        
        def bfs(node):
            seen = set()
            q = deque()
            q.append(node)
            
            arr = []
            
            while (len(q) != 0):
                currentSize = len(q)
                currentLevel = []
                
                for i in range(currentSize):
                    current = q.popleft()
                    currentLevel.append(current.val)
                           
                    if (current.left is not None):
                        q.append(current.left)
                    if (current.right is not None):
                        q.append(current.right)
                    
                print(currentLevel)
                arr.append(currentLevel)
                
            return arr
                    
        
        
        return bfs(root)
            