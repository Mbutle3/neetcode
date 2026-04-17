class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = []

        start = 0

        current_product = 0

        for end in range(len(nums)):
            start += end
            while start < len(nums):
                current_product *= nums[start]
                start += 1
            products.append(current_product)
        return products