from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if (root is None):
            return []
        
        def bfs(node):
            q = deque()
            q.append(node)
            way = True
            arr = []
            
            # 
            while (len(q) != 0):
                currentSize = len(q)
                currentLevel = deque()
                
                # Loop through the current level queue
                for i in range(currentSize):
                    current = q.popleft()

                    # Check the way to see if we pop left or right from the queue
                    if way:
                        currentLevel.append(current.val)
                    else:
                        currentLevel.appendleft(current.val)
                        
                    # Add the left and right nodes for the next level queue
                    if (current.left is not None):
                        q.append(current.left)
                    if (current.right is not None):
                        q.append(current.right)
                
                # Swap the way
                way = not way
                arr.append(currentLevel)
            return arr

        return bfs(root)
                