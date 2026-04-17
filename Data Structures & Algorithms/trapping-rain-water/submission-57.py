class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        LMax = height[L]
        RMax = height[R]
        mostWaterTrapped = 0
        currentWaterTrapped = 0

        while L < R:
            if LMax < RMax:
                L += 1
                if LMax < height[L]:
                    LMax = max(LMax, height[L])
                    currentWaterTrapped += LMax - height[L]
            else:
                R -= 1
                if RMax < height[R]:
                    RMax = max(RMax, height[R])
                    currentWaterTrapped += RMax - height[R]
            mostWaterTrapped = max(currentWaterTrapped, mostWaterTrapped)
        return mostWaterTrapped


         
        