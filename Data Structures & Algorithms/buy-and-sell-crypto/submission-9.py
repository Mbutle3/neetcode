class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = float('-inf')
        max_profit = 0
        n = len(prices)

        for i in range(1, n):
            current_profit = prices[i] - prices[i - 1]
            min_profit = min(current_profit, min_profit)
            max_profit = max(current_profix, max_profit)
        return max_profit

        