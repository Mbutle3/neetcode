class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0 
        right = 1
        seen = {}

        for left, val in enumerate(nums):
            while left - right > k:
                seen.remove(nums[left])
                left += 1
            if nums[right] in window:
                if nums[left] == nums[right]:
                    return True
            seen.add(nums[left])
        return False
            


            