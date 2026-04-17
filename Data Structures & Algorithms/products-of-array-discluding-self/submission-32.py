class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = 1 * [0]

        prefix = 1
        for i in range (n):
            prefix *= res[i]
            nums[i] *= prefix 
            
        
        postfix = 1
        for i in range (n - 1, -1, -1):
            postfix *= res[i]
            nums[i] *= postfix
        
        return res
            



