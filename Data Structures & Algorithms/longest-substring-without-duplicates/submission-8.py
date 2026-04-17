class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLen = 0
        left = 0

        for char, right in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            maxLen = max(maxLen, right - left + 1)
        return maxLen