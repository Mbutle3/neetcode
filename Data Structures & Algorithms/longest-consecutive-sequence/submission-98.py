class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longestSeq = 0

        for num in setNums:
            currentSeq = 1
            key = num + 1
            while key in setNums:
                currentSeq += 1
                key -= 1
            longestSeq = max(longestSeq, currentSeq)
        return longestSeq
                    


        