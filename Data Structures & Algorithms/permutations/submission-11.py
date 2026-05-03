class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []

        def backtrack(i):
            res.append(perms.copy())
            
            for j in range(i, len(nums)):
                perms.append(nums[j])
                backtrack(j + 1)
                perms.pop()
        backtrack(0)
        return res