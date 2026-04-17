class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start].isalpha().lower() != s[end].isalpha().lower():
                return False
            else:
                start += 1
                end -= 1
        return True

        