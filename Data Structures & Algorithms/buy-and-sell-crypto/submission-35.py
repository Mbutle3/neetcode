class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for price in prices[1:]:
            current_profit = price - buy
            max_profit = max(max_profit, current_profit)
            buy = min(buy, price)
        return max_profit