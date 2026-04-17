class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)

        while L < R:
            mid = (L + (R - L)) // 2
            if mid == target:
                return mid
            elif mid < target:
                L = mid + 1
            else:
                R = mid - 1
        return -1

        