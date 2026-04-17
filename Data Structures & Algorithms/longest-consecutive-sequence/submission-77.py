class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        foundSequence = 0
        longestFound = 0

        for num in nums:
            while num + 1 in seen:
                 foundSequence += 1
            else:
                longestFound = max(longestFound, foundSequence)
                seen.add(num)

        return longestFound
        