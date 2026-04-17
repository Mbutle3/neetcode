class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        LMax = height[L]
        RMax = height[R]
        trappedWater = 0
        while L < R:
            if LMax < RMax:
                LMax = max(LMax, height[L])
                trappedWater += LMax - height[L]
                L += 1
            else:
                RMax = max(RMax, height[R])
                trappedWater += RMax - height[R]
                R -= 1
        return trappedWater


