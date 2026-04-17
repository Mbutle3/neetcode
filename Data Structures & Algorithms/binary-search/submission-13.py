class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 1
        end = len(nums) -1

        while start <= end:
            mid_point = (start + end) // 2

            if nums[mid_point] == target:
                return mid_point
            elif nums[mid_point] < target:
                start += 1
            elif nums[mid_point] > target:
                end -= 1
        return -1

        