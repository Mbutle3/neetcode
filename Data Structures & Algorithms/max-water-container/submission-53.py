class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        leftMax = heights[left]
        right = len(heights) - 1
        rightMax = heights[right]
        
        res = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                if leftMax < height[left]:
                    leftMax = max(leftMax, height[left])
                res += max(res, right - left + 1)
            else:
                right -= 1
                if rightMax < heigh[right]:
                    rightMax = max(rightMax, height[right])
                res += max(res, right - left + 1)
        return res
                
        