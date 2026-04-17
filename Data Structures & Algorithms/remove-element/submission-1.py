class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0

        for i in range(nums):
            if nums[i] != val:
                nums[idx] = nums[i]
        return idx
        