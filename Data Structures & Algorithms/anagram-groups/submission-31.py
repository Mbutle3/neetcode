class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i in range(len(strs)):
            sorted_word = sorted(strs[i])

            if sorted_word not in seen:
                seen[strs[i]] = [sorted_word]
            else:
                seen[strs[i]].append(sorted_word)
        return seen.values()

        