class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mxProfit = 0
        buy = prices[0]
        for price in prices[1 :]:
            current_profit = price - buy
            mxProfit = max(mxProfit, current_profit)
            buy = min(buy, current_profit)
        return mxProfit
        