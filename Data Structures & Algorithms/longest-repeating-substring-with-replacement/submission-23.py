from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        left = 0
        right = 0  
        majority_ele = 0 
        seen = defaultdict(int)

        while right < n:
            seen[right] += 1
            right += 1
            while majority_ele + k < right - left + 1:
                seen[left] += 1
                left += 1
            majority_ele = max(majority_ele, right - left + 1)
        return majority_ele




        
        