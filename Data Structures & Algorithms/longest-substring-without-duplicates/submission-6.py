class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        maxLen = 0 

        for right, char in enumerate(s):
            if char in seen:
                left = seen[char] + 1
            seen[char] = right
            maxLen = max(maxLen, right - left + 1)
        return maxLen
        