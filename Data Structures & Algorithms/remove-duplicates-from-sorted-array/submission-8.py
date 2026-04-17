class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        index = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[i + 1]:
                nums[index] = nums[i]
                index += 1
        return index