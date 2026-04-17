class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        seen = set(nums)

        for num in seen:
            if num - 1 not in seen:
                length = 1
                curr = num

                while curr + 1 in seen:
                    curr += 1
                    length += 1
                longest = max(longest, length)
        return longest