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
            while j < len(candidates):
                while j > i and candidates[j] == candidates[j - 1]:
                    j += 1
                combos.append(candidates[j])
                dfs(j + 1, combos, currSum + candidates[j])
                combos.pop()

        dfs(0, [], 0)
        return res
        

        