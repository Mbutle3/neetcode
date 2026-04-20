class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorderDFS(node):
            if not node:
                return
            inorderDFS(node.left)
            res.append(node.val)
            inorderDFS(node.right)
        inorderDFS(root)
        return res[k-1]