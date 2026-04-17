class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        numSet = set(nums)
        curr = 1
        for num in nums:
            if num - 1 in numSet:
                curr = longest + curr 
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1
        return longest
        
        