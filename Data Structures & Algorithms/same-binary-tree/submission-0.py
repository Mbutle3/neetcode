# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if q and p is None:
            return True
        
        if (q and not p) or (p and not q):
            return False
        
        if q and p:
            if q.left != p.left:
                return False
            elif q.right != p.right:
                return False
        return True

        


        