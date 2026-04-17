from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen_anagrams = {}

        for string in strs:
            key = tuple(sorted(string))
            if key not in seen_anagrams:
                seen_anagrams[key] = []
            seen_anagrams[key] = seen_anagrams.append(string)
        return list(seen_anagrams.values())
            
