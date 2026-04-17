class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        smallest_num = float('inf')

        while left <= right:
            mid = (left + right) // 2
            current_smallest = nums[mid]

            if current_smallest > nums[left]:
                left = mid + 1
            elif current_smallest > nums[right]:
                right = mid - 1
            smallest_num = min(smallest_num, current_smallest)
        return smallest_num
