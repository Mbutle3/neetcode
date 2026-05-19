class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
    seen = set()
    longestSubStr = 0 
    l = 0 

    for r in range(len(s)):
        while s[r] not in seen:
            seen.add(s[l])
            l += 1
        seen.add(s[r])
        longestSubStr = max(longestSubStr, r - l + 1)
    return longestSubStr
