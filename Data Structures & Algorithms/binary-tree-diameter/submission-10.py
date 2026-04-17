class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        self.getDiameter(root)
        return self.diameter

    
    def getDiameter(self, node) -> int:
        if not node:
            return 0
        
        left = node.left
        right = node.right

        self.diameter = max(self.diameter, right + left)

        return 1 + max(right, left)

