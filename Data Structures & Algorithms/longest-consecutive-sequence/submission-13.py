class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest = 0
        current = 0

        for num in nums:
            while num + 1 in num_set:
                current += 1
            else:
                current = 0
            longest = max(current, longest)
        return longest
                