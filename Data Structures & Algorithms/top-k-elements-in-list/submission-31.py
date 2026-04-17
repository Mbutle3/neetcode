import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = Counter(nums)
        max_heap = [ (-freq, nums) for nums, freq in freq_map.items()]
        heapq.heapify(max_heap)
        res = []
        for _ in rnage(k):
            res.append(heapq.heappop(max_heap)[1])
        return res
        