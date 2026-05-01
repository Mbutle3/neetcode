class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        leftMax = heights[left]
        right = len(heights) - 1
        rightMax = heights[right]
        
        res = 0

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            res = (right - left) * min(heights[left], heights[right])
        return res
                
        