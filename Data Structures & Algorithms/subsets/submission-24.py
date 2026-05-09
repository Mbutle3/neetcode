class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        res = []
        def backtrack(i):
            res.append(subsets.copy())

            for j in range(len(nums)):
                subsets.append(nums[j])
                backtrack(j + 1)
                subsets.pop()
        backtrack(0)
        return res
        