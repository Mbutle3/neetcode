class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = {}

        for w in strs:
            sorted_w = tuple(sorted(w))
            if sorted_w not in words:
                words[sorted_w] = [w]
            else:
                words[sorted_w].appennd(w)
        
        return list(words.values())



        