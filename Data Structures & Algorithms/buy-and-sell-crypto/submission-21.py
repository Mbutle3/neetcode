class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for price in prices:
            current_profit = buy - price
            max_profit = max(max_profit,current_profit)
            buy = min(buy, price)
        return max_profit
        