class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window_max = max(nums[:k])
        cache = window_max
        max_window = nums[: k]

        for i in range(1, len(nums) - k + 1):
            window_max = max(nums[i + k - 1], window_max)
            if window_max != cache:
                max_window = nums[: i + k - 1]
                cache = window_max
        return max_window

        