# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0
            stack = [root, 1]
            balanced = 0
            while stack:
                node, curr = stack.pop()
                left = dfs(root.left, curr + 1)
                right = dfs(root.right, curr + 1)
                balanced = 1 if left[0] and right[0] and abs(left[1] - right[1]) <= 1 else 0
            return balanced
        dfs(root)
        return root[0]


        