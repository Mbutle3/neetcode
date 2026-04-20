# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderDFS(root, k):
            stack = []       # starts empty
            curr = root      # pointer starts at root
            while stack or curr:
                while curr:              # drill left, push as you go
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()       # process: next smallest
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right        # move right
        return inorderDFS(root, k)