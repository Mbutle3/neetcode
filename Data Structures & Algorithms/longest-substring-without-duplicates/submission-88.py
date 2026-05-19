class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set() #declaring set to keep track of chars we encounter
        l = 0  # left pointer to build substring width
        longest = 0  #longest substring found

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        return longest


