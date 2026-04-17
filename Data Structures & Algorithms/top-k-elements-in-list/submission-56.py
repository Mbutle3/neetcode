import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        min_heap = [ (freq, num) for num, freq in freq_map.items() ]
        heapq.heapify(min_heap)

        res = []
        n = len(min_heap)
        for _ in range(n - k):
            res.append(heapq.heappop(min_heap)[1])
        return res