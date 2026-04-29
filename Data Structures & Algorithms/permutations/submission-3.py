class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(permSize, perms):
            if permSize > len(nums):
                return
            if len(perms) == len(nums):
                res.append(perms.copy())

            for j in range(len(nums)):
                if nums[j] not in perms:
                    perms.append(nums[j])
                    dfs(j, perms)
                    perms.pop()
                    
        dfs(0, [])
        return res
        