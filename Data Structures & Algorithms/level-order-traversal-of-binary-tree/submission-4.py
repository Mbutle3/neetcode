# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.arr = []
        self.levelOrderHelper(root)
        return root
    
    def levelOrderHelper(self, root)-> List[List[int]]:
        if not root:
            return None
        val = root.val
        self.arr.append([val])
        left = self.levelOrderHelper(root.left)
        right = self.levelOrderHelper(root.right)

        return self.arr
        

         