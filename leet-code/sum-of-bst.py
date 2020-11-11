class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0
        def traverse(node: TreeNode):
            if (node is None):
                return
            traverse(node.left)
            if (node.val >= low and node.val <= high):
                self.ans += node.val
            traverse(node.right)
            
        traverse(root)
        return self.ans