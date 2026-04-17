class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        seen = set()
        left = 0 
        n = len(s) 

        for right in range (n):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left)
        return longest
        

        