class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, perms):
            if perms not in res:
                res.append(perms.copy())

            for j in range(i, len(nums)):
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
                perms.append(nums[j])
                dfs(j + 1, perms)
                perms.pop()
        dfs(0, [])
        return res