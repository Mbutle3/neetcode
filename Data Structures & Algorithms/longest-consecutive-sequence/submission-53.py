class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in numSet:
                length = 1
                curr = num + 1
                while curr - 1 in numSet:
                    length += 1
                    curr += 1
                longest = max(longest, length)
        return longest
