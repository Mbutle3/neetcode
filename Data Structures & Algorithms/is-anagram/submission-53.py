class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        
        #If strings have different lengths 
        if len(s) != len(t):
            return False
        
        seen = {}

        for char in s:
            if char not in seen:
                seen[char] = 1
        
        for char in t:
            if char not in seen:
                return False #str t has diff chars than str s
            seen[char] -= 1
            
            if seen[char] == 0:
                del seen[char]
        
        return len(seen) == 0
        

        