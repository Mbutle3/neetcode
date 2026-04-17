class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s)

        while start < end:
            if s[start] != s[end]:
                return False
            elif s[start].isalum() == s[end].isalnum():
                start += 1
                end -= 1
        return True
        