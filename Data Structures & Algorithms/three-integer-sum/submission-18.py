
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return
        res = [list]
        seen = {}
        n = len(nums) - 1
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    val = nums[i] + nums[j] + nums[k]
                    if (val == 0 and (nums[i] != nums[j] and num[i] != nums[k] and nums[j] !=  nums[k])):
                        res.append([nums[i], nums[j], nums[k]])
        return res
                    




        