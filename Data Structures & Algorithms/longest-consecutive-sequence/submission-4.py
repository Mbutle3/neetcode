class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        current_min = min(nums)
        LCS = 1
        MAX_LCS = 1
        i = 0

        while i < len(nums):
            j = i 
            while j < len(nums):
                if nums[j] == current_min + 1:
                    MAX_LCS = max(LCS, MAX_LCS)
                    j = i + 1
                else:
                    j += 1
            i += 1
            current_min=nums[i]
        return MAX_LCS

        


