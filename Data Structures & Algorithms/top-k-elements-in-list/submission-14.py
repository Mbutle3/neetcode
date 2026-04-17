class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []

        for n in nums:
            if n not in seen:
                seen[n] = 1
            else:
                seen[n] += 1
        
        for k, v in seen.items():
            if v > k:
                res.append(k)
                del k
        
        return res