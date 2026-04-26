class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = collections.Counter(tasks)
        maxHeap = [-(v) for v in freqMap.values()]
        heapq.heapify(maxHeap)

        queue = deque()

        time = 0

        while maxHeap or queue:
            time += 1

            if not maxHeap:
                time = queue[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time




        