from typing import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orderd_map = defaultdict(list)
        for word in strs:
            key = sorted(tuple(word))
            orderd_map[word].append([key])
        return list(ordered_map.values())


        