class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res : List[List[int]] = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1

            while l < r:
                triplet = nums[i] + nums[l] + nums[r] 
                if triplet < 0:
                    i += 1
                elif triplet > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1
                    r -= 1
                    while l < r and nums[i] == nums[i - 1]:
                        i += 1
                    while l < r and nums[r] == nums [r + 1]:
                        r += 1
            return res
                    