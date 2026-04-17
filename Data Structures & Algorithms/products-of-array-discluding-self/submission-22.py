class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        n = len(nums)
        prefix = 1
        for i in range(n):
            prefix *= nums[i]
            res[i] = prefix

        postfix = 1
        for i in range(n-1, -1, -1):
            postfix *= nums[i]
            res[i] = postfix
            
        return res

        