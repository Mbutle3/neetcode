from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:                      # s1 can't fit in s2
            return False

        need = Counter(s1)             # counts we need
        window = Counter(s2)       # first window of size n

        if window == need:
            return True

        for i in range(n, m):
            add = s2[i]
            rem = s2[i - n]
            window[add] += 1
            window[rem] -= 1
            if window[rem] == 0:
                del window[rem]        # keep dicts comparable
            if window == need:
                return True

        return False
