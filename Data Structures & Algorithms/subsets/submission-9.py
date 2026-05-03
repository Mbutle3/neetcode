class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def backtrack(i):
            res.append(subsets.copy())

            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
        backtrack(nums)
        return res
        