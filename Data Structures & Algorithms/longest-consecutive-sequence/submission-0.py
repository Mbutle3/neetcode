class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)

        return_seq_len = float('-inf')
        found_seq = float('-inf')

        for digit in nums:
            if (digit in nums_set) and (digit + 1 in nums_set):
                found_seq += 1
            else:
                found_seq = 0
                return_seq_len = max(found_seq, return_seq_len)
        return return_seq_len

        