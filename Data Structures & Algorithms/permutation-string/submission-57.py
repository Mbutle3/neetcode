from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False
        
        count_s1 = Counter(s1)
        count_window = Counter(s2[: l1])

        if count_window == count_s1:
            return True

        for right in range (l2):
            start_char = s2[right - l1]
            new_char = s2[right]

            if count_window[start_char] == 0:
                del count_window[start_char]
            
            if count_window == count_s1:
                return True
        return False

            