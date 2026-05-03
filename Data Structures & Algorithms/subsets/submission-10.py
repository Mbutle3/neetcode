class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def backtrack(i):
            res.append(subsets.copy())

            for j in range(len(nums)):
                subsets.append(nums[j])
                dfs(j + 1)
                subsets.pop()
        backtrack(nums)
        return res
        