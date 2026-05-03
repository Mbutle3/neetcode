class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backTrack(i):
            res.append(subset.copy())

            for j in range(i, len(nums)):
                subset.append(nums[j])
                backTrack(j + 1)
                subset.pop()
        backTrack(0)
        return res
        