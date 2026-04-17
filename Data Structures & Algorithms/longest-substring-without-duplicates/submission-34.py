class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        seen = set()
        longest = 0 
        n = len(s)

        for right in range (n):
            if s[right] not in seen:
                seen.remove(s[left])
                l += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        return longest

        