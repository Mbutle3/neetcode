class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combos = []

        def backtrack(i, total):
            if total == target:
                res.append(combos.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            for j in range(i, len(nums)):
                combo.append(nums[j])
                backtrack(j, total + nums[j])
                combo.pop()
        backtrack(0,0)
        return res
        