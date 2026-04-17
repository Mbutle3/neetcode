class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = 0
        rightMax = 0
        left = 0
        right = len(height) - 1
        water_trapped = 0

        while left <= right:
            if height[l] <= height[r]:
                if leftMax <= height[l]:
                    leftMax = height[l]
                else:
                    water_trapped += leftMax - height[l]
                l += 1
            else:
                if rightMax <= height[r]:
                    rightMax = height[r]
                else:
                    water_trapped += rightMax - height[r]
                r -= 1
        return water_trapped

        