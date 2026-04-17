import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        min_heap = [ (freq, num) for num, freq in freq_map.items() ]
        heapq.heapify(max_heap)

        res = []
        n = len(nums)
        for _ in range(n, k, -1):
            res.append(heapq.heappop(max_heap)[1])
        return res