import heapq
from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        max_heap = [(-freq, num) for num, freq in freq_map.items()]
        heapq.heapif(max_heap)

        res = []

        for i in range(k):
            res.append(heapfiy.popleft[1])
        return res
        