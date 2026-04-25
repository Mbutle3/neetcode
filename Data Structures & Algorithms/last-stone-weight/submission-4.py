class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -maxHeap.heappop()
            x = -maxHeap.heappop()

            if x < y:
                heapq.heappush(maxHeap, y - x)
        return -maxHeap[0] if maxHeap else 0
        