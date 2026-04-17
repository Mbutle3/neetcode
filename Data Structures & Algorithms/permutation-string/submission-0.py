class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if (s2 and not s1) or (s1 and not s2):
            return False
        
        seen = {}

        for char in s2:
            seen[char].get(char, 0) + 1
        
        for char in s1:
            if char not in seen:
                return False
            elif char in seen:
                seen[char] -= 1
            elif char[seen] == 0 and char == char[seen]:
                return False
            elif char[seen] == 0:
                del char[seen]
        return True
            

        

        
        