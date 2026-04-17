# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = False
        self.getHeight(root)
        return self.balanced
        
    def getHeight(self, node):
        if not node:
            return 0
        
        left = node.left
        right = node.right

        self.getHeight(left)
        self.getHeight(right)

        if ((right - left == 1) or (left - right == 1)):
            self.balanced = True
       
        