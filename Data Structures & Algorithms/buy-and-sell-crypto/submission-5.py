from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables
        min_price = -1 # Set to a very large value
        max_profit = 0  # Start with 0 profit
        
        # Iterate through prices
        for price in prices:
            # Update the minimum price seen so far
            min_price = min(min_price, price)
            # Calculate profit if sold at current price and update max profit
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
