# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preorder(root, maxV):
            if not root:
                return 0
            stack = [root]
            while stack:
                node = stack.pop()
                maxVal = node.val
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                
                good = 1 if (preorder(node.left, maxVal) or preorder(node.right, maxVal)) else 0
            return good
        return preorder(root, root.val)


            