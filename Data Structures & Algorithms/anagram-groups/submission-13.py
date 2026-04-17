class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen_anagrams = {}

        for string in strs:
            key = seen_anagrams[key]
            if key not in seen_anagrams:
                seen_anagrams = []
            seen_anagrams[key].append(string)    
        return list(seen_anagrams.values())
        