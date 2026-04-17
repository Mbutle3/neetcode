class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 
        while num - 1 in numSet:
            length = 1 
            curr = num + 1
            while curr in numSet:
                curr += 1
                length += 1
            longest = max(longest, length)
        return longest

