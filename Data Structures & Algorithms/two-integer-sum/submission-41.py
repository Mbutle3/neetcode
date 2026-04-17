class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for idx, val in enumerate(nums):
            compliment = target - val
            if compliment in seen:
                return [idx, seen[compliment]]
            else:
                seen[val] = idx
        return [-1, -1]
        