# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(root):
            if not root:
                return 
            q = deque([root])
            while q:
                curr = q.popleft()
                curr.left,curr.right = curr.right, curr.left
                if curr.left:
                    curr = curr.left
                if curr.right:
                    curr = curr.right
            return root
        return bfs(root)
        
