class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0 
        charSet = set(s)

        for char in charSet:
            left = 0 
            count = 0 

            for right in range (n):
                if s[right] == char:
                    count += 1

                    while (right - left + 1) - count > k:

                        if s[left] == char:
                            count -= 1
                        left += 1
                        res = max(res, right - left + 1)
        return res
        
        