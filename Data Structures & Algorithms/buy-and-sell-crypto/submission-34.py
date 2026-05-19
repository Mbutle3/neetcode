class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for price in prices[1:]:
            current_profit = price - buy
            buy = min(buy, price)
            max_profit = max(max_profit, current_profit)
        return max_profit