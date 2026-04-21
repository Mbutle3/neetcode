class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: i for i, val in enumerate(inorder)}

        def helper(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r or in_l > in_r:
                return None

            val = preorder[pre_l]
            root = TreeNode(val)
            mid = indices[val]

            left_size = mid - in_l

            root.left  = helper(pre_l + 1, pre_l + left_size, in_l, mid - 1)
            root.right = helper(pre_l + left_size + 1, pre_r, mid + 1, in_r)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)