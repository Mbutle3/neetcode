class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def dfs(i):
            if i > len(nums):
                res.append(subset.copy())
                return
            subset.append(nums)
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        