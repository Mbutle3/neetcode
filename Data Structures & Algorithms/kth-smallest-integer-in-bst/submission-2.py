# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderDFS(root, k):
            if not root:
                return 0
            stack = []
            curr = root
            while stack or curr:
                while curr:
                    node = stack.pop()
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                    k -= 1
                    if k == 0:
                        return curr.val
            return -1
        return inorderDFS(root, k)
        