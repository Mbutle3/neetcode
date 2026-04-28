class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, combos, currSum):
            if i >= len(nums) or currSum > target:
                return
            
            combos = nums[i]
            currSum = sum(nums[: i])

            res.append(dfs(i + 1, combos,currSum))

        dfs(nums, [], 0)
        return res