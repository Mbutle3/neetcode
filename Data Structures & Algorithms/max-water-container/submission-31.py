class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        current_area = 0
        l = 0
        r = len(heights) - 1
        n = len(heights) - 1
        for i in range (n):
            current_area = min(current_area, r - l + 1) * (r - l)
            max_area = max(current_area, max_area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area
        