class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest_seq = 0 

        for num in nums:
            length = 1
            curr = num
            while curr - 1 in numSet:
                length += 1
                curr += 1
            longest = max(length, longest)
        return longest



        