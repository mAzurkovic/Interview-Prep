class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        biggerVals = []
        vals = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if (node.val > p.val):
                biggerVals.append(node)
                vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        if (len(biggerVals) == 0):
            return None
        else:
            get = min(vals)
            for i in biggerVals:
                if i.val == get:
                    return i