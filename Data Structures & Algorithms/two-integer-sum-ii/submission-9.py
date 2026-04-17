class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for idx, val in enumerate(numbers):
            compliment = val - target
            if compliment in seen:
                return [seen[compliment] + 1, idx + 1]
            else:
                seen[val] = idx
        return [-1, -1]
        