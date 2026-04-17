class Solution:
    def search(self, nums: List[int], target: int) -> int:

        s = 0
        e = len(nums) - 1
        m = (s + e) // 2

        while s <= e:
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s+=1
            else:
                e-=1
        return -1

            