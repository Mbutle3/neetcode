class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0
        currentWater = 0
        L = 0
        for R in range(len(heights)):
            currentWater = min(heights[L], heights[R]) * R - L
            mostWater = max(mostWater, currentWater)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return mostWater
        