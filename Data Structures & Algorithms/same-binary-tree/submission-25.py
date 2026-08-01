# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def inOrder(x, arr):
            if x is None:
                return 
            inorder(x.left)
            arr.append(x.val)
            inorder(x.right)
        
        inOrder(p, arr1)
        inorder(q, arr2)

        return arr1 == arr2        