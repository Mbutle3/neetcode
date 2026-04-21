# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Base Case
        if not preorder or not inorder:
            return None
        
        #Get root
        val = preorder[0]
        root = TreeNode(val)

        #Get mid
        mid = inorder.index(val)

        inorder_left = inorder[: mid]
        inorder_right = inorder[mid + 1 :] #skip mid itself, that's the root

        preorder_left = preorder[1 : mid + 1] #skip root, take next `mid` elements
        preorder_right = preorder[mid + 1 :] # everything after the left chunk

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, preorder_right)

        return root



        