class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_count_one = {}
        freq_count_one = {}

        for val in s:
            if val not in freq_count_one:
                freq_count_one[val] = 1
            else:
                freq_count_one[val] += 1

        for val in t:
            if val in freq_count_one:
                freq_count_one[val] -= 1
        return freq_count_one == 0
