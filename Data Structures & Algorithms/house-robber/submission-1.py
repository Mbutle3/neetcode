class Solution:
    def rob(self, nums: List[int]) -> int:

        if nums is None:
            return 0
        
        max_profits = 0 
        i = 0
        
        while i <= len(nums):
            current_profit = max(self.rob(nums[i + 1]), self.rob(nums[i - 1]))
            i += 1
        max_profits(current_profit, max_profit)
        return max_profits