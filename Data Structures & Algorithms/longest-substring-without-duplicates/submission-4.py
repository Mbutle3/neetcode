class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0 
        n = len(s)
        charSet = set()

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - 1 + 1)
        return res