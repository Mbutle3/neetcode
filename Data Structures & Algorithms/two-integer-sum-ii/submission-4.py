class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for idx, val in enumerate(numbers):
            compliment = val - target
            if compliment in seen:
                return [compliment[val], idx]
            else:
                seen[val] = idx
        return [-1, -1]
        