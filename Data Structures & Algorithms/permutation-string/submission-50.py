from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_1 = len(s1)
        len_2 = len(s2)

        if len_1 > len_2:
            return False
        
        count_s1 = Counter(s1)
        count_window = Counter(s2[: len_1])

        if count_s1 == count_window:
            return True

        for i in range (len_1, len_2):
            start_char = s2[i - len_1]
            new_char = s2[i]

            count_window[start_char] -= 1

            if count_window[start_char] == 0:
                del count_window[start_char]
            
            count_window[new_char] += 1

            if count_s1 == count_windoow:
                return True
        return False
