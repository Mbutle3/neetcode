class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Dictionary to count character frequencies
        freq_count = {}

        # Count characters in the first string
        for char in s:
            freq_count[char] = freq_count.get(char, 0) + 1

        # Subtract counts based on the second string
        for char in t:
            if char not in freq_count:
                return False
            freq_count[char] -= 1

        # Ensure all counts are zero
        return len(freq_count) == 0
