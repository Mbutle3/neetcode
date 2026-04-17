class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        length = 0 
        seen = set()
        left = 0 
        n = len(s) - 1
        for right in range (n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        return longest


        