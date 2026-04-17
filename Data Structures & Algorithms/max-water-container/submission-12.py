class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights) - 1
        container_with_most_water = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            container_with_most_water = max(container_with_most_water, area)

            l += 1
            r -= 1
        return container_with_most_water
