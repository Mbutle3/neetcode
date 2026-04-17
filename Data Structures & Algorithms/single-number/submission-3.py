class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res ^= set(nums)

        return res

        