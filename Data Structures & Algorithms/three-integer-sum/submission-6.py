class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        seen = {}

        for n in nums:
            if n not in seen:
                seen[n] = 1
            else:
                seen[n] += 1
        print(seen.items())

        return []