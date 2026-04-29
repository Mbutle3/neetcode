class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, perms):
            if i > len(nums):
                return 
            if perms not in res:
                res.append(perms.copy())

            for j in range(i, len(nums)):
                if nums[j] == nums[j - 1]:
                    continue
                perms.append(nums[j])
                dfs(j, perms)
                perms.pop()
        dfs(0, nums)
        return res