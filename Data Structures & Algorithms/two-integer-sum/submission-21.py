class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for index, val in enumerate(nums):
            compliment = target - val
            if val in seen:
                return [seen[compliment], index]
            seen[compliment] = index
        return [-1,-1]