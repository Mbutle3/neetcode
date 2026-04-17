class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0 
        n = len(s)
        seen = set()

        for right in range (n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[left])
            longest = max(longest, right - left + 1)
        return longest
