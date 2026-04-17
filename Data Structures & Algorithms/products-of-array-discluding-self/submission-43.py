class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix, postfix, length =  1, 1, len(nums)
        
        res = [1] * length

        for i in range(length):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(length - 1, -1, -1):
            res[i] *= prefix
            postfix *= nums[i]
        
        return res
        
        