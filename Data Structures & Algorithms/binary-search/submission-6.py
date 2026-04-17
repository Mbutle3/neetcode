class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0

        end = len(nums) -1

        while start <= end:
            mid_point = (start + end) // 2

            if target > mid_point:
                start += 1
            elif target < mid_point:
                end -= 1
            if target == mid_point:
                return mid_point
        return -1
        