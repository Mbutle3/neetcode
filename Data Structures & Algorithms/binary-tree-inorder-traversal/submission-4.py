def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
        
    res = []
    res += self.inorderTraversal(root.left)
    res.append(root.val)
    res += self.inorderTraversal(root.right)
    return res