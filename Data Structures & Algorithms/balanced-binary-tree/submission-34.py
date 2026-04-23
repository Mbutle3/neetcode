# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True
            left_bal, left_height = dfs(node.left)
            right_bal, right_height = dfs(node.right)

            balanced = left_bal and right_bal
            height = 1 + max(left_height, right_height)

            return balanced, height
        return dfs(root)[0]
        