class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == reversed(s)
        