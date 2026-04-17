class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        left = 0
        longest = 0

        for right in range (n):
            if s[right] in seen:
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
