# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minNodeVal(root, val):
        curr = root
        while curr and curr.left:
            curr = curr.next
        return curr
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None
        
        if val > root.val:
            root.right = self.deleteNode(root.right, val)
        if val < root.val:
            root.left = self.deleteNode(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minNodeVal(root.right)
                root.val = minNode.val
                root.right = self.deletNode(root.right, minNode)
        return root