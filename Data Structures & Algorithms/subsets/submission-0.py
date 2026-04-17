class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set(ans)
        
        if not nums:
            return ans
        
        for n in nums:
            if self.subsets(n) not in seen:
                ans.append(self.subsets(n))
                seen.add(ans)
        return ans


        