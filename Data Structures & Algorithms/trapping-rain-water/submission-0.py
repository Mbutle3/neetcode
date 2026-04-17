class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        
        l = 0 
        r = len(heights) - 1

        leftMax = height[l]
        rightMax = height[r]

        most_trapped_water = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                most_trapped_water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                most_trapped_water += rightMax - height[r]
        return most_trapped_water

        