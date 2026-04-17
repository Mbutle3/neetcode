class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_sub_string_len_found = 0 
        left = 0 

        for right in range (s[:]):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest_sub_string_len_found = max(longest_sub_string_len_found, right - left + 1)
        return longest_sub_string_len_found

        