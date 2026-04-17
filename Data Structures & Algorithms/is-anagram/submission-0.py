class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p1 = 0
        p2=len(t) - 1

        while (p1 <= p2):
            if s[p1] == t[p2]:
                p1+=1
                p2+=1
                continue
            else:
                return False
        return True


        