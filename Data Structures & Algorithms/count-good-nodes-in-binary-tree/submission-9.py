# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0
            good = 1 if root.val < maxVal else 0
            dfs(root.left, root.val)
            dfs(root.right, root.val)
            return good
        return dfs(root, root.val)
        