class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0 
        right = 1
        seen = set()

        for left, val in enumerate(nums):
            while abs(left) - abs(right) > k:
                seen.remove(nums[left])
                left += 1
            if nums[right] in seen and nums[left] == nums[right]:
                return True
            else:
                seen.add(nums[right])
        return False
            


            