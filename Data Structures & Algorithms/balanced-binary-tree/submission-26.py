# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, curr):
            if not root:
                True
            left = dfs(root.left, curr + 1)
            right = dfs(root.right, curr + 1)
            if abs(left - right) <= 1:
                return True
            return False
        return dfs(root, root.val)
        