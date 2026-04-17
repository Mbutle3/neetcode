class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = 0

        seen = {}

        for v in nums:
            if nums not in seen:
                seen[nums] = 1
            else:
                seen[nums] += 1
        
        return list(v for v in seen.values() > k)
        