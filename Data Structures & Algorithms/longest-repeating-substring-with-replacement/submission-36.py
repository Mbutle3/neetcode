from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_len = 0 
        left = 0
        right = 0 
        n = len(s)
        major_ele = 0
        count_map = defaultdict(int)

        while right < n:
            right_val = s[right]
            seen[right_val] += 1
            major_ele = max(major_ele, seen[right_val])
            while major_ele + k < right - left + 1:
                left_val = s[left]
                seen[left_val] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
