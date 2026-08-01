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
                arr.append(None)
                return
            inOrder(x.left, arr)
            arr.append(x.val)
            inOrder(x.right, arr)
        
        inOrder(p, arr1)
        inOrder(q, arr2)

        return arr1 == arr2        