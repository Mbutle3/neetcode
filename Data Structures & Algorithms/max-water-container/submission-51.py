class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0 
        currentWater = 0 
        L = 0
        R = len(heights) - 1
        while L < R:
            currentWater = min(heights[L], heights[R]) * (R - (R-L))
            mostWater = max(currentWater, mostWater)
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        return mostWater
        