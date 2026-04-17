from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict()
        left = 0 
        right = 0
        max_len = 0
        major_ele = 0

        while right < len(s):
            #find major ele
            major_ele = s[right]
            major_ele = max(major_ele, s[right])
            while major_ele + k < right - left + 1:
                max_len = max(max_len, right - left + 1)
                left += 1
            right += 1
        return max_len

