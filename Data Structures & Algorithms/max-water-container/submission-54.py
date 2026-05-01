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
                if leftMax < heights[left]:
                    leftMax = max(leftMax, heights[left])
                res += max(res, right - left + 1)
            else:
                right -= 1
                if rightMax < heigh[right]:
                    rightMax = max(rightMax, heights[right])
                res += max(res, right - left + 1)
        return res
                
        