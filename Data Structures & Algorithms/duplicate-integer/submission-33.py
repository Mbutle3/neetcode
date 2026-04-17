class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1
        return nums
        