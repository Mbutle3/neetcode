class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        l = 0
        r = len(height) - 1
        left_max = 0
        right_max = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    trapped += max(left_max, height[l]) * (r - l)
                l += 1
            else:
                if height[r] > right_max:
                    right_max = height[r]
                else:
                    trapped += max(right_max, height[r]) * (r - l)
                r -= 1
        return trapped


        