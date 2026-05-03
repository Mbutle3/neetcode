class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subsets = []

        def backtrack(i):
            res.append(subsets.copy())
    
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                subsets.append(nums[j])
                backtrack(j + 1)
                subsets.pop()
        backtrack(0)
        return res
