class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        n = len(s)
        seen = set()
        length = 0
        for right in range (n):
            if s[right] not in seen:
                seen.add(s[right])
            seen.remove(s[left])
            left += 1
            max_len = max(max_len, left - right + 1)
        return max_len
        