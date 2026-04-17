class Solution:
    def isPalindrome(self, s: str) -> bool:

        s.lower() #1. set all characters to lowercase

        left = 0 
        right = len(s) - 1

        while left < right:
            while s[left].isalpha == False and left < right:
                left += 1
            while s[right].isalpha == False and left < right:
                right -= 1
            
            if s[left].isalpha != s[right].isalpha:
                return False
            else:
                left += 1
                right -= 1
        return True


        

        