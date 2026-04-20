# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0]
        def inorderDFS(root):
            nonlocal res
            if not root:
                return 0
            inorderDFS(root.left)
            
            res.append(root.val)

            inorderDFS(root.right)
        inorderDFS(root)
        return res[k]
        