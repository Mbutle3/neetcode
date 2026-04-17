class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0
        l = 0 
        r = 0
        left_max = 0 
        right_max = 0 

        while l <= r:
            if height[l] <= height[r]:
                if left_max <= height[l]:
                    left_max = height[l]
                else:
                    water_trapped += left_max - height[l] * (r - l + 1)
                l += 1
            else:
                if right_max <= height[r]:
                    right_max = height[r]
                else:
                    water_trapped += right_max - height[r] * (r - l + 1)
                r -= 1
        return water_trapped
        