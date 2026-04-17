class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest_seq = 0 

        for num in nums:
            if num - 1 not in seen:
                length = 1
                curr = num + 1
                while curr in seen:
                    length += 1
                    curr += 1
                longest_seq = max(longest_seq, length)
        return longest_seq



        