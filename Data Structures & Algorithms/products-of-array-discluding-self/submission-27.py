class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = 1 * [0]

        prefix = 1
        for i in range (n):
            nums[i] *= prefix 
            prefix *= res[i]
        
        postfix = 1
        for i in range (n):
            nums[i] *= postfix
            postfix *= res[i]
        
        return res
            



