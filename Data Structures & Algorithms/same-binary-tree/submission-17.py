# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeChecker(self, root):
        if not root:
            return None
        left = self.treeChecker(root.left)
        right = self.treeChecker(root.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and q:
            return False
        if not q and p:
            return False
        
        if not q and not p:
            return True

        check_p_left = self.treeChecker(p.left) 
        check_p_right = self.treeChecker(p.right) 

        check_q_left = self.treeChecker(q.left) 
        check_q_right = self.treeChecker(q.right) 

        return check_p_left == check_q_left and check_p_right == check_q_right
        