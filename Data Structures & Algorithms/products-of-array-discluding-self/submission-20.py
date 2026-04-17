class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        n = len(nums)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] = prefix
            postfix *= nums[i]

        return res

        