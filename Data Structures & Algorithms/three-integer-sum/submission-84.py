class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        e = len(nums) - 2
        res = []

        while i < e :
            l = i + 1
            r = e - 1
            
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val < 0:
                    r -= 1
                elif val > 0:
                    l += 1
                else:
                    res.append(nums[i], nums[l], nums[r])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res

        