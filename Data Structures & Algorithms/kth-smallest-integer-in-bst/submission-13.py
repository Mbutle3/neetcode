# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderDFS(node, k):
            stack = []
            curr = root
            while stack or curr:
                while curr:
                    if curr:
                        curr = curr.left
                    stack.append(curr.val)
                    curr = curr.right
                    k -= 1
                    if k == 0:
                        return curr
        return inorderDFS(root, k)