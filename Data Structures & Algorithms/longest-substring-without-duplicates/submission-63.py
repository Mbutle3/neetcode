from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0 
        right = 0 
        max_len = 0 
        n = len(s)
        
        for right in range (n):
            while s[right] in seen:
                seen.remove([s[left]])
                left += 1 
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
        