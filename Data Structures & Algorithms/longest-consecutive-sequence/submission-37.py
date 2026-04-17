class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        uniqueNums = set(nums)
        for num in nums:
            if num - 1 in uniqueNums:
                length = 1
                while num + length in uniqueNums:
                    lenght += 1
                longest = max(lenght, longest)
        return longest
            
        