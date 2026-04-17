class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
   
        idx = 0
        last_val = nums[-1]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i - 1]
                idx += 1
        nums.append(last_val)
        return idx
        