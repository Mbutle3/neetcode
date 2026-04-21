from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        def dfs(root):
            if not root:
                return None
            # swap left and right subtrees
            root.left, root.right = root.right, root.left
            # recurse into each subtree
            dfs(root.left)
            dfs(root.right)
            return root
        
        def bfs(root):
            if not root:
                return None
            q = deque([root])
            while q:
                curr = q.popleft()
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            return root
            
        return bfs(root)