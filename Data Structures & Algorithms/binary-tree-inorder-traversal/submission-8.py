# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []

        def inOrder(x):
            if x is None:
                return 
            left = inOrder(x.left)
            res.append(x.val)
            right = inOrder(x.right)

        inOrder(root)
        return res
        