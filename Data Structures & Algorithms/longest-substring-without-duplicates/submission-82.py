class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longestSubString = 0 
        L = 0 
        for R in range(len(s)):
            if s[R] in seen:
                seen.remove(s[L])
                L += 1
            else:
                seen.add(s[R])
                longestSubString = max(longestSubString, R - L)
        return longestSubString
        