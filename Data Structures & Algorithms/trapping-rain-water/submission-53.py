class Solution:
    def trap(self, height: List[int]) -> int:
        mostTrappedWater = 0 
        trappedWater = 0 
        L = 0
        R = len(height) - 1
        LMax = height[L]
        RMax = height[R]

        while L < R:
            if LMax < RMax:
                if LMax < height[L]:
                    LMax = max(LMax, height[L])
                    trappedWater += LMax - height[L]
                else:
                    L += 1
            else:
                if RMax < height[R]:
                    RMax = max(RMax, height[R])
                    trappedWater += RMax - height[R]
                else:
                    R -= 1
            mostTrappedWater = max(mostTrappedWater, trappedWater)
        return mostTrappedWater
            
                    

        