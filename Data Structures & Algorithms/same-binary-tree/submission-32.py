class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def preOrder(x, arr):
            if x is None:
                arr.append(None)
                return
            arr.append(x.val)
            preOrder(x.left, arr)
            preOrder(x.right, arr)

        preOrder(p, arr1)
        preOrder(q, arr2)

        return arr1 == arr2