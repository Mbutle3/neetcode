class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_count = {}

        for char in s:
            if char not in freq_count:
                freq_count[char] = 1
            else:
                freq_count[char] += 1
        
        for char in t:
            if char not in freq_count:
                return False
            else:
                freq_count[char] -= 1
        
        if len(freq_count) == 0:
            return True
        return False


