import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = ""
        self.nums = []
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        heapq.heapify(self.nums)
        
        for i in range(val):
            if i == val:
                return self.nums[i]
                break
        
