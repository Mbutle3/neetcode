from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0 
        od = defaultdict(int)
        n = len(s)
        major_element = 0
        longest = 0

        if n < k:
            return 0
        
        for right in range (n):
            od[s[right]] += 1
            major_element = max(major_element, od[s[right]])
            while major_element + k < right - left + 1:
                od[s[left]] += 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest


        