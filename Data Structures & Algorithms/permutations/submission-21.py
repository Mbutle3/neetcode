class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []

        def backtrack(i):
            if len(perms) == len(nums):
                res.append(perms.copy())
                return
            
            for num in nums:
                if num not in perms:
                    perms.append(num)
                    backtrack(perms)
                    perms.pop()
        backtrack(0)
        return res
        