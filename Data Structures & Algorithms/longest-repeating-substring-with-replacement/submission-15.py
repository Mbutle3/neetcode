from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0 
        right = 0
        max_len = 0 
        majority_ele = 0 
        count_map = defaultdict(int)
        
        while right < n:
            count_map[s[left]] -= 1
            majority_ele = max(majority_ele, count_map[s[left]])
            while majority_ele + k < right - left + 1:
                left += 1
                count_map[s[right]] += 1
            max_len = max(max_len, right - left + 1)
            right -= 1
        return max_len
