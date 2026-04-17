class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False
            if s[start].isalnum() == s[end].isalnum():
                start += 1
                end -= 1
        return True
        