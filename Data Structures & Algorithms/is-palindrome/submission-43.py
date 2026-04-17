class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start <= end:
            while s[start].isalpha() == False:
                start += 1
            while s[end].isalpha() == False:
                end -= 1
            
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
            


        