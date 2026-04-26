class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = collections.Counter(tasks)
        maxHeap = [-(v) for v in freqMap.values()]
        heapq.heapify(maxHeap)

        queue = deque()

        time = 0

        while maxHeap or queue:
            time += 1
            if maxHeap or queue:
                time += 1
                if maxHeap:
                    freq = 1 + heapq.heappop(maxHeap)
                    if freq != 0:
                        queue.append([freq, time + n])
                    if queue and queue[0][1] <= time:
                        heapq.heappush(maxHeap, queue.popleft()[0])
        return time






        