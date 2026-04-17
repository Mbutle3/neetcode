class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, val in enumerate(nums):
            compliment = val - target

            if compliment in seen:
                return [seen[compliment], i]
            else:
                seen[val] = i
        return [-1,-1]
        