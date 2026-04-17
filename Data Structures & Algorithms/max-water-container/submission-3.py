class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0
        n = len(heights)
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, min(heights[i], heights[j])) * (j - i)
        return res