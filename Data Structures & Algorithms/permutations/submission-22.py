class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []

        def backtrack():
            if len(perms) == len(nums):
                res.append(perms.copy())
                return
            
            for num in nums:
                if num not in perms:
                    perms.append(num)
                    backtrack(perms) #what does this do? search for other nums? since we are here do we only hit perms.pop() once we discovered all other nums not in perm?
                    perms.pop() #we remove to readd the same number later in the program?
        backtrack()
        return res
        