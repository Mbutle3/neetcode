# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []

        def preOrder(x):
            if x is None:
                return
            res.append(x.val)
            preOrder(x.left)
            preOrder(x.right)
        preOrder(root)
        
        return res