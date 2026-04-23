# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def dfs(root, curr):
            nonlocal maxSum
            if not root:
                return 0, 0
            leftCurrSum += dfs(root.left, root.val)
            rightCurrSum += dfs(root.right, root.val)
            currSum = (
                    sum(leftCurrSum, rightCurrSum) 
                        if leftCurrSum + rightCurrSum > leftCurrSum or leftCurrSum + rightCurrSum > rightCurrSum  
                        else max(leftCurrSum, rightCurrSum)
                    )
            maxSum = max(currSum, maxSum)
            return maxSum
        return dfs(root, maxSum)
        