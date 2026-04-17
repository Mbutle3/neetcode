class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        
        foundSequence = 0
        longestFound = 0

        for num in nums:
            
            startingPoint = num - 1

            if startingPoint not in uniqueNums:
                foundSequence = 1
                curr = startingPoint + 1

                while curr in uniqueNums:
                    curr += 1
                    foundSequence += 1

            longestFound = max(longestFound, foundSequence)
            
        return longestFound
        