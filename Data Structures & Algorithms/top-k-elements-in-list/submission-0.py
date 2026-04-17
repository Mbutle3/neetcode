class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        heap = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappush(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappush(heap)[1])
        return res
