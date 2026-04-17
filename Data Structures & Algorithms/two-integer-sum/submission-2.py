class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = 0
        e = len(nums) - 1

        nums.sort()

        while s <= e:
            if nums[s] + nums[e] == target:
                return [s,e]
            elif nums[s] + nums[e] > target:
                e -= 1
            else:
                s += 1
        return [-1,-1]