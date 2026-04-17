class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLen = 0
        left = 0

        for right, char in enumerate(s):
            if char in seen and seen[char]:
                maxLen = max(maxLen, right - seen[char])
            else:
                seen[char] = right
        return maxLen
        