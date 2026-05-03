class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combos = []
        def backtrack(i, combo):
            res.append(combos.copy())

            for j in range(len(nums)):
                if sum(combo) == target:
                    combos.append(combo)
                combo.append(nums[j])
                backtrack(j + 1, combo)
        backtrack(0, [])
        return res
        