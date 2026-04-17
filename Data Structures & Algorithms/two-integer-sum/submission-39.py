class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for current_idx in range(len(nums)):
            compliment = target - nums[current_idx]
            if compliment in seen:
                return [seen[compliment], current_idx]
            else:
                seen[current_num] = current_idx
        return [-1, -1]
        