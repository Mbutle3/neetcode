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
            q = collections.deque([root])
            depth = 0
            currDepth = 0
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    currDepth += 1
                depth = max(currDepth, depth)
            return depth
        return bfs(root)

        