class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values_seen = {}

        for current_index, current_val in enumerate(nums):
            missing_val = target - current_val
            
            if missing_val in values_seen:
                return [values_seen[missing_val], index]

            if current_val not in values_seen:
                values_seen[current_val] = current_index

        return[-1, -1]
            

            