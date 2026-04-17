class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area_of_water = 0 
        l = 0 
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r - 1)
            water_collected = max(max_area_of_water, max_area_of_water)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r-= 1
        return max_area_of_water
        