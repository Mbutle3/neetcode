class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        n = len(nums) 
        
        #prefix pass
        prefix = 1
        for i in range(n):
            res[i] = prefix
            pres *= nums[i]
        #postfix pass
        postfix = 1

        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
