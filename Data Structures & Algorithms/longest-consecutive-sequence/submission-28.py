class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        seq = 1
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            if num + 1 in seen:
                seq += 1
                longest = max(seq, longest)
            
        return longest
        