class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0
        self.getDiameter(root)
        return self.diameter

    
    def getDiameter(self, node) -> int:
        if not node:
            return 0
        
        left = self.getDiameter(node.left)
        right = self.getDiameter(node.right)

        self.diameter = max(self.diameter, left + right)

        return 1

