class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        seen = {}

        for n in nums:
            if n not in seen:
                seen[n] = [n]
            else:
                seen[n].append(n)
        print(seen)

             