class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n

        firstPass = 1
        for i in range(n):
            res[i] *= firstPass
            firstPass  *= nums[i]

        secondPass = 1
        for i in range(n):
            res[i] *= secondPass
            secondPass  *= nums[i]
        return res

        