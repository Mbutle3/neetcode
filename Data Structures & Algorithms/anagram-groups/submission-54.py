from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            if not key in words:
                words[key] = []
            else:
                words[key].append(word)
        return list(words.values())