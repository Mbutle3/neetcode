class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            L = idx + 1
            R = len(nums) - 1
            while L < R:
                total = val + nums[L] + nums[R]
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                else:
                    res.append([val, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
        return res

        