class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(perms):
            if len(perms) > len(nums):
                return
            if len(perms) == len(nums):
                res.append(perms.copy())

            for j in range(len(nums)):
                if nums[j] not in perms:
                    perms.append(nums[j])
                    dfs(perms)
                    perms.pop()
                    
        dfs([])
        return res
        