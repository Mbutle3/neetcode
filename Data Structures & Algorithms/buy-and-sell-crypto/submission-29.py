class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]
        for currentPrice in prices[1:]:
            currentProfit = currentPrice - buyPrice
            maxProfit = max(currentPrice, currentPrice)
            buyPrice = min(buyPrice, currentPrice)
        return maxProfit



        