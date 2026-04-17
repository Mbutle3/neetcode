class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_count = {}

        for val in s:
            if val not in freq_count:
                freq_count[val] = 1
            else:
                freq_count[val] += 1

        for val in t:
            if val in freq_count:
                freq_count[val] -= 1
            else:
                return False
        return freq_count == 0
