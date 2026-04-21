# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return None
            #swap left and right trees
            root.left, root.right = root.right, root.left
            #swap left subtrees
            if root.left:
                self.invertTree(root.left)
            #swap right subtrees
            if root.right:
                self.invertTree(root.right)
            #return transformed root
            return root

        return dfs(root)