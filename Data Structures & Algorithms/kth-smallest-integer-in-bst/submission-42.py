# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return 0
            stack = []
            curr = root
            arr = []
            while stack or curr:
                while curr:
                    arr.append(curr.val)
                    if curr.left:
                        stack.append(curr.left)
                        curr = curr.left
                    if curr.right:
                        stack.append(curr.right)
                        curr = curr.right
            return arr[k - 1]
        return inorder(root)
        