class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []

        def backtrack():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return 
            
            for num in nums:
                if num in perms:
                    continue
                perms.append(num)
                backtrack()
                perms.pop()

        backtrack()
        return res
        