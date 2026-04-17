class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 1 
        for num in numSet:
            curr = num - 1
            while curr in numSet:
                curr += 1
                length += 1
            longest = max(longest, length)
        return longest

