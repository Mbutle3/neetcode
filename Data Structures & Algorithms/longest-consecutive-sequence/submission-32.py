class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        numSet = set(nums)
        for num in nums:
            if num - 1 not in numSet:
                curr = 1
                while num + curr in seen:
                    curr += 1
                longest = max(longest, curr)
        return longest

        