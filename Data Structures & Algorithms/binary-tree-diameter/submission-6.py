# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.balanced = True
        self.diameter = 0
        self.height(root)
        return root
    
    def height(self, node) -> int:
        if not node:
            return 0
        
        left = self.height(node.left)
        right = self.height(node.right)

        if abs(right - left) > 1:
            self.balanced = False
        
        largest = max(right, left)

        return 1 + max(self.diameter, largest)

        

        