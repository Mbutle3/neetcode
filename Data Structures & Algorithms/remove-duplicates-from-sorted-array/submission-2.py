class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        index = 0
        for n in nums:
            if n not in seen:
                index += 1
                nums[index] = n
        return index