class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def backtrack(i):
            res.append(subsets.copy())

            for j in range(i, len(nums)):
                subsets.append(nums[j])
                backtrack(j + 1)
                subsets.pop()
        backtrack(0)
        return res