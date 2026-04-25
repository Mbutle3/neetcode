class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(x ** 2, y ** 2, x, y) for x,y in points]
        heapq.heapify(minHeap)

        ans = []

        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            ans.apeend([x,y])
        return ans
        