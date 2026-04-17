class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) == 0 and len(t) != 0 ) or (len(s) != 0 and len(t) == 0 ):
            return False 
        if len(s) == 0 and len(t) == 0:
            return True
        
        seen = {}

        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        
        for char in t:
            if char not in seen:
                return False
            else:
                seen[char] -= 1
            if seen[char] == 0:
                del char
        return True

        