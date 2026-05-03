class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combos = []

        def backTrack(i, total):
            if total == target:
                res.append(combos.copy())
                return
            
            if total > target or i >= len(nums):
                return

            for j in range(i, len(nums())):
                combos.append(nums[j])
                backTrack(j + 1, total + nums[j])
                combos.pop()
        backTrack([], 0)
        return res

        