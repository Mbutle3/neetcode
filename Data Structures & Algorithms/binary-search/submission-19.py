class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        idx = 0
        
        while L < R:
            if nums[L] < target:
                L += 1    
            else:
                R -= 1
            idx += 1
            if nums[L] == target:
                return idx
        return -1
            
        