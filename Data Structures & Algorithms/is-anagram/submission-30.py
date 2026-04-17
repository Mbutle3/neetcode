class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_count = {}

        for char in s:
            if char not in freq_count:
                freq_count[char] = freq_count.get(char, 0) + 1
        
        for char in t:
            if char not in freq_count:
                return False
            else:
                freq_count[char] -= 1
            if freq_count[char] == 0:
                del freq_count[char]
        
        return len(freq_count) == 0