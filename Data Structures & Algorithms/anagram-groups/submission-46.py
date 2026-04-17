from typing import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orderd_map = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            ordered_map[word].append([key])
        return list(ordered_map.values())


        