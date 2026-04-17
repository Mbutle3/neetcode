class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest_seq = 0 

        for num in nums:
            length = 1
            curr = num
            while curr - 1 in numsSet:
                length += 1
                curr += 1
            longest_seq = max(length, longest_seq)
        return longest_seq



        