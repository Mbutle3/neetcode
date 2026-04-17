class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.height(root)
        return self.diameter

    def height(self, node: Optional[TreeNode]):
        if not node:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        # update best diameter through this node (edges)
        self.diameter = max(self.diameter, left + right)

