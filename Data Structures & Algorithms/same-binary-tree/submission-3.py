# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.arr = []
        arr1 = self.dfs(p)
        arr2 = self.dfs(q)

        return arr1 == arr2
    
    def dfs(self, root):
        if not root:
            return None
        
        val = root.val
        self.arr.append(val)

        self.dfs(root.left)
        self.dfs(root.right)

        return self.arr
        