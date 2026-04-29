class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, combos, currSum):
            if currSum == target: #HAPPY CASE
                res.append(combos.copy())
                return 
            if i > len(nums) or currSum > target: #Sad Case
                return
            
            dfs(i, combos, currSum + nums[i])
            combos.pop()

            dfs(i + 1, combos, currSum)

        dfs(0, [], 0)
        return res
            