class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        n = len(nums)

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        