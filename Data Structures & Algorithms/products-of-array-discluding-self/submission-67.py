class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n

        firstPass = 1
        for i in range(n):
            res[i] *= nums[i]
            firstPass *= nums[i]

        secondPass = 1
        for i in range(n - 1, -1, -1):
            res[i] *= nums[i]
            secondPass *= nums[i]
        return res

        