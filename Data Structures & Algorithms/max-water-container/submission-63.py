class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0
        MaxArea = 0
        while left < right:
            currentArea = (right - left) * min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            MaxArea = max(MaxArea, currentArea)
        return MaxArea
                
        