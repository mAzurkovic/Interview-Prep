from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if (root is None):
            return 0
        
        def dfs(node):
            levels = 0
            q = deque()
            q.append(node)
            
            while (len(q) != 0):
                size = len(q)
                
                for i in range(size):
                    current = q.popleft()
                    print(current.val)
                    if (current.left is not None):
                        q.append(current.left)
                    if (current.right is not None):
                        q.append(current.right)
                
                levels += 1
            return levels
    
        return dfs(root)