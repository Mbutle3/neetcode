class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        middle_point = len(nums) // 2


        while start < end:
            if nums[middle_point] == target:
                return middle_point
            elif target > middle_point:
                start = middle_point
                start += 1
            elif target < middle_point:
                end = middle_point
                end -= 1
        return - 1
        



        