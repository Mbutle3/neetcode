class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)
        left_max = 0
        right_max = 0
        trapped = 0 

        while l < r:
            if left_max < right_max:
                if height[l] >= left_max:
                    left_max = max(left_max, height[l])
                else:
                    trapped += left_max - height[l]
                i += 1
            else:
                if height[r] >= right_max:
                    right_max = max(right_max, height[r])
                else:
                    trapped += right_max - height[r]
                r -= 1
        return trapped

        