class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0

        maxF = 0

        n = len(s)

        for right in range (n):
            char = s[right]
            
            count[char] = 1 + count.get(char, 0)
            maxF = max(maxF, count[char])

            while (right - left + 1) - maxF > k:
                count[char] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res