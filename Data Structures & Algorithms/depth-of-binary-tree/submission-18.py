# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            if not root: 
                return 0
            resDepth = 0
            currDepth = 0
            q = collections.deque([root])
            while q:
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    currDepth += 1
                if curr.right:
                    q.append(curr.right)
                    currDepth += 1
                resDepth = max(currDepth, resDepth)
            return 1 + resDepth
        return bfs(root)
                
        