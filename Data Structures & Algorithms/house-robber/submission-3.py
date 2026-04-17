class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}

        if nums is None:
            return 0
        
        i = 0
        while i <= len(nums):
            current_profit = self.rob(nums[i] - 1) - self.rob(nums[i] - 2)
            cache[i] = current_profit
        return max(cache.values())
