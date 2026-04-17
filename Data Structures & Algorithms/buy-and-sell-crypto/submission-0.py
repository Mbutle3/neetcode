class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 0

        for i in range(1,len(prices)):
            buy = max(buy, prices[i-1])
            sell = min(sell, prices[i-1])
        return buy - sell