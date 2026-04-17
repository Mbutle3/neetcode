class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment == target:
                return {i, seen[compliment]}
            seen[i] = compliment
        return {-1, -1}
        