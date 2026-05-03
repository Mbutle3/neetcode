class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []

        def backtrack(i, n):
            if n == len(nums):
                res.append(perms.copy())
                return 
            
            for j in range(i, len(nums)):
                perms.append(nums[j])
                backtrack(j, nums + 1)
                perms.pop()
        backtrack(0,0)
        return res
        