class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = i
        return index