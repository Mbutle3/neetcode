class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen_chars = {}

        for char in s:
            seen_chars[char] = seen_chars.get(char, 0) + 1
        
        for char in t:
            if char not in seen_chars:
                return False
            else:
                seen_chars[char] -= 1
            if seen_chars[char] == 0:
                del seen_chars[char]
        return True
        