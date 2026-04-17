class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        mostWater = 0
        waterCollected = 0
        while L < R:
            waterCollected = min(height[L], height[R]) * (R - L)
            mostWater = max(mostWater, waterCollected)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return mostWater
