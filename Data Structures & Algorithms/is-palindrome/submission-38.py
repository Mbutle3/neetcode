class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start].isalnum() != s[end].isalnum():
                return False
            elif s[start].isalnum() == s[end].isalnum():
                start += 1
                end -= 1
        return True
        