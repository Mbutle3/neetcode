class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []

        def backtrack(i, n):
            if n == len(nums):
                res.append(perms.copy())
                return 
            
            perms.append(nums[i])
            backtrack(i + 1, n + 1)
            perms.pop()
        backtrack(0,0)
        return res
        