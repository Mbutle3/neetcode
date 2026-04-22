# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            stack = [root]
            curr = root
            arr = []
            while stack or curr:
                while curr:
                    node = stack.pop()
                    if node.left:
                        stack.append(node.left)
                    arr.append(node.val)
                    if node.right:
                        stack.append(node.right)
            return arr[k - 1]
        return inorder(root)
        