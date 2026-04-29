class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, perms):
            if i > len(nums):
                return
            if i == len(nums):
                res.append(perms)
            perms.append(nums[i])
            dfs(i, perms)
            perms.pop()
            dfs(i + 1, perms)
        dfs(nums)
        return res
        