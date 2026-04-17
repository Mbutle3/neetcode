class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_keeper = {}

        for char in t:
            freq_keeper[char] = freq_keeper.get(char, 0) + 1

        for char in s:
            if char not in freq_keeper:
                return False
            else:
                freq_keeper[char] -= 1
            if freq_keeper[char] == 0:
                del freq_keeper[char]
        
        return freq_keeper == 0
        