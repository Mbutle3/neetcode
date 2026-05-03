class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []

        def backtrack():
            # we've filled every slot, save the completed permutation
            if len(perms) == len(nums):
                res.append(perms.copy())
                return
            
            # try every number in nums as a candidate for the current slot
            for num in nums:
                # skip it if we already used it in the current path
                if num not in perms:
                    
                    # choose: add this number to the current slot
                    perms.append(num)
                    
                    # explore: go fill the next slot with whatever's left
                    # this will keep recursing until all slots are filled
                    backtrack()
                    
                    # UN-choose: remove it so we can try the next candidate
                    # this is what "backtracking" actually means
                    # we're climbing back up to try a different path
                    perms.pop()
        backtrack()
        return res
        