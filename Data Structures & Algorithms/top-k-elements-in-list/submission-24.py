class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        seen = {}

        for n in nums:
            if n not in seen:
                seen[n] = 1
            else:
                seen[n] += 1
        
        
        vals = list(seen.values())

        res = []
        for v in vals:
            if v >= k:
                res.append(v)
        
        return res

