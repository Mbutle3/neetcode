class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0
        currentWater = 0
        n = len(heights) - 1
        L = 0
        for R in range(n):
            currentWater = min(heights[L], heights[R]) * R - L
            mostWater = max(mostWater, currentWater)
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        return mostWater
        