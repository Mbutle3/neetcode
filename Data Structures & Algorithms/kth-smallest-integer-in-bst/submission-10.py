# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorderDFS(node):
            self.inorderDFS(node.left)
            res.append(node.val)
            self.inorderDFS(node.right)
        inorderDFS(root)
        return res[k - 1]
        