class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []
        products = []
        start = 0
        for i in range(len(nums)):
            current_val = nums[i]
            while start + 1 < (len(nums)):
                start += 1
                current_val *= nums[start]
            products.append(current_val)
        return products

