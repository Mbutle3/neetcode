class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_vals = {}

        for current_index, current_val in enumerate(nums):
            compliment = target - current_val
            if compliment in seen_vals:
                return [seen_vals[compliment], current_index]
            if current_val not in seen_vals:
                seen_vals[current_val] = index
        return [-1,-1]
        