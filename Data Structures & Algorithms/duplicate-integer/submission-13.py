class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dups = set(nums)

        return len(no_dups) == len(nums)
         