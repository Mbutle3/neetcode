class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                continue
            else:
                return True
        return False