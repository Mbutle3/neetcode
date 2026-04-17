class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l_pointer, r_pointer = 0, len(s) - 1

        while l_pointer < r_pointer:
            while l_pointer < r_pointer and not s[l_pointer].isalnum():
                l_pointer += 1
            while l_pointer < r_pointer and not s[r_pointer].isalnum():
                r_pointer -= 1

            if s[l_pointer].upper() != s[r_pointer].upper():
                return False
        return True
