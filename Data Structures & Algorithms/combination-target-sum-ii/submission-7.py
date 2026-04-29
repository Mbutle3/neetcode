class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: 
        res = []
        candidates.sort()
        def dfs(i, combos, currSum):
            if currSum == target:
                res.append(combos.copy())
                return
            if i >= len(candidates) or currSum > target:
                return
            j = i
            for j in range (i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                combos.append(candidates[j])
                dfs(j + 1, combos, currSum + candidates[j])
                combos.pop()

        dfs(0, [], 0)
        return res
        

        