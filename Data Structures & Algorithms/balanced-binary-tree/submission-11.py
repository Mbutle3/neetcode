# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.balanceChecker(root)
        return self.balanced
    
    def balanceChecker(self, node):
        if not node:
            return False
        
        left = self.balanceChecker(node.left)
        right = self.balanceChecker(node.right)

        if abs(right - left) > 1:
            self.balanced = False
        return

        