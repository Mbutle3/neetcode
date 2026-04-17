class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        largest_seq = 0
        current_seq = 0

        i = 0
        seen = {(set)}
        n = len(nums)

        while i < n:
            j = i
            while j < n:
                if nums[j] + 1 in seen:
                    current_seq += 1
                else:
                    seen[j].add(nums[j])
                largest_seq = max(largest_seq, current_seq)
            i = j + 1
        return largest_seq
                



        