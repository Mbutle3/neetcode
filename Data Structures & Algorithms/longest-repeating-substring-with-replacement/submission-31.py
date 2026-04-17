from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        left = 0 
        right = 0 
        max_len = 0
        major_ele = 0
        seen = defaultdict(int)

        while right < n:
            seen[s[right]] -= 1
            major_ele = max(major_ele, seen[s[right]])
            left += 1
            while major_ele + k < right - left + 1:
                seen[s[left]] += 1
                max_len = max(max_len, right - left + 1)
            right += 1
        return max_len

