class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def backtack(i):
            res.append(subsets.copy())

            for j in range(i, len(nums)):
                subsets.append(nums[j])
                backtack(i + 1)
                subsets.pop()
        backtack(0)
        return res
        
        