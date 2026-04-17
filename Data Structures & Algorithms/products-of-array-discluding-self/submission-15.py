class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        current_sum = 0

        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                current_sum *= nums[j]
                j += 1
            res.append[current_sum]
            i += 1
        return res
        