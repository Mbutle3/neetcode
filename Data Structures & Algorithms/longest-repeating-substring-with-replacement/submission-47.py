from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0 
        right = 0 
        max_area = 0 
        major_ele = 0 
        seen = defaultdict(int)

        while right < n:
            seen[s[right]] += 1
            major_ele = max(major_ele, seen[s[right]])
            while major_ele + k < right - left + 1:
                seen[s[left]] -= 1    
                left += 1
            max_area = max(max_area, right - left + 1)
            seen[s[left]] += 1
            right += 1
        return max_area