from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False
        
        count_s1 = Counter[s1]
        counter_window = Counter(s2[: len1])

        if count_s1 == count_window:
            return True
        
        for i in range (len1,  len2):
            start_char = s2[i - len1]
            new_char = s2[i]
            count_window[start_char] -= 1

            if count_window[start_char] == 0:
                del count_window[start_char]
            
            count_window[new_char] += 1

            if count_window == count_s1:
                return True

        return False


        