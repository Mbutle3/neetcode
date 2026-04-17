from collections import Counter, deque
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freqMap = [(-k,v) for key, val in enumerate(nums.items())]
        print(freqMap)