# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            save = None 
            for _ in range(len(q)):
                node = q.popleft()
                save = max(node.left.val, node.right.val)
                if node.left:
                    q.append(node.left)
                if right.left:
                    q.append(node.left)
            ans.append(save.val)
        return ans
