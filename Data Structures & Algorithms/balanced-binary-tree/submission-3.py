# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.getHeight(root)
        return self.balanced
        
    def getHeight(self, node):
        if not node:
            return 0
        
        left_height = getHeight(node.left)
        right_height = getHeight(node.right)

        if abs(left - right) > 1:
            self.balanced = False

        return 1 + max(left, right)
        
        