class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_string = s.lower()
        start = 0
        end = len(lower_string) - 1

        while start <= end:
            if lower_string[start].isalpha() != lower_string[end].isalpha():
                return False
            else:
                start += 1
                end -= 1
        return True

        