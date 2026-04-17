from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        orderd_map = defaultdict()

        for word in strs:
            key = tuple(sorted(word))
            orderd_map[key]+=[word]
        return list(orderd_map.values())
        