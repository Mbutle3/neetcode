class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0 
        left = 0 
        right = len(height) - 1
        left_max = 0 
        right_max = 0

        while left < right:
            if height[left] <= height[r]:
                if left_max <= height[l]:
                    left_max = height[l]
                else:
                    water_trapped += left_max - height[l]
                left += 1
            else:
                if right_max <= height[r]:
                    right_max = height[r]
                else:
                    water_trapped += right_max - height[r]
                right -= 1
        return water_trapped
        