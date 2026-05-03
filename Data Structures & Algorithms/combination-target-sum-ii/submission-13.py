class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combos = []

        def backtrack(i, total):
            if total == target:
                res.append(combos.copy())
                return 
            if total > target or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if candidates[j] == candidates[j -1]:
                    continue
                combos.append(candidates[j])
                backtrack(j + 1, total + candidates[j])
                combos.pop()
        backtrack(0,0)
        return res

        