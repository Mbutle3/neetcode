class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        seen = {}
        for num in nums:
            seq = 1
            if num not in seen:
                seen[num].add(num)
            if num + 1 in seen:
                seq += 1
                longest = max(seq, longest)
        return longest
        