class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            l = i + 1 
            r = n - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]

                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
                
