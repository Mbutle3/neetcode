class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        left_max = 0
        r = len(height) - 1
        right_max = 0
        n = r
        water_collected = 0 
        
        while l < r:
            if height[l] < height[r]:
                if left_max < height[l]:
                    left_max = height[l]
                else:
                    water_collected += height[l] - left_max
                l += 1
            else:
                if right_max < height[r]:
                    right_max = height[r]
                else:
                    water_collected += height[r] - right_max
        return water_collected


        