class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        left = 0 

        right = 0

        n = len(nums)

        max_found = float('-inf')


        seen = {}

        while right < n:

            while nums[right] not in seen and right < k:
                seen[nums[right]] += 1
                max_found = max(max_found, seen[nums[right]])
                right += 1
            seen[nums[left]] += 1
            left += 1
        return max_found
            

