class Solution:
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        res = []
        
        # build first window
        window_sum = max(nums[:k])
        res.append(window_sum)
        
        # slide
        for i in range(1, len(nums) - k + 1):
            window_max = max(nums[i:i+k])  # O(k) each time — not ideal
            res.append(window_max)
        
        return res

            