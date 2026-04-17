class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        res = 0
        left = 0 
        n = len(s)
        for right in range(n):
            freq[ord(s[right]) - ord('A')] += 1
            while (right - left + 1) - max(freq) > k:
                freq[ord(s[right]) - ord('A')] -= 1
                left += 1
            res = max(res, right - left)
        return res


        