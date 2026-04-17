class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = []

        start = 0

        current_product = 0

        for end in range(len(nums)):
            start += end
            while start < len(nums):
                product *= nums[start]
            products.append(product)
        return products