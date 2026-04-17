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

        for k, val in seen.items():
            current_sum = key
            if (i,j) in seen.values():
                if current_sum + i + j == 0:
                    res.append(k, seen[i], seen[j])
            val -= 1
        return res