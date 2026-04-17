class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == set(nums):
            return True
        return False
         