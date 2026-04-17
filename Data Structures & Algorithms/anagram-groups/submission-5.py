from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen_anagrams = {}

        for i in range(len(strs)):
            if strs[i] not in seen_anagrams:
                key = tuple(sorted(strs[i]))
            seen_anagrams[key] = seen_anagrams.append(strs[i])
        return list(seen_anagrams.values())