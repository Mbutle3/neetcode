class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []
        products = []
        start = 0
        current_val = nums[0]
        for i in range(len(nums)):
            while start + 1 < min(len(nums), i):
                start += 1
                currnet_val *= nums[start]
            products.append(current_val)
        return products

