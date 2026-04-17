class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []
        products = []
        final_val = 0
        start = 0
        for i in range(len(nums)):
            current_val = nums[i]
       
            while start + 1 < min(len(nums), i):
                start += 1
                current_val *= nums[start]
                final_val = max(final_val, current_val)
            products.append(final_val)
        return products

