class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        #build first window
        window_sum = max(nums[: k])
        res.append(window_sum)

        #slide 
        for i in range(1, len(nums)):
            window_max = max(window_sum, len(nums) - k + 1)
            res.append(window_max)
        return res

        