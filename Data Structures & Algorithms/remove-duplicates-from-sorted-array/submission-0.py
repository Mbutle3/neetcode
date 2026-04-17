class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        index = 0
        for n in nums:
            if n in seen:
                continue
            else:
                nums[index] = n
        return nums
        