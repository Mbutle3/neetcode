class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen = {}

        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
        
        for c in t:
            if c not in seen:
                return False
            elif c in seen and seen[c] != 0:
                seen[c] -= 1
            else:
                del seen[c]
        
        return True
        

        