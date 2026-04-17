class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        seen = set()
        max_len = 0

        for right in range(len(s)):
            if s[right] in seen:
                left += 1
                seen.remove(s[left])
            max_len = max(max_len, left - right + 1)
        return max_len
