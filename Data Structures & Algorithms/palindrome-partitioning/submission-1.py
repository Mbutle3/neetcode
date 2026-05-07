class Solution:

    def isPalidrome(self, word) -> bool:
        l = 0
        r = len(word) - 1

        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        palidromes = []
        def backtrack(i, palidromes):
            if i == len(s):
                res.append(palidromes.copy())
            
            for j in range(i, len(s)):
                subString = s[i : j + 1]
                if self.isPalidrome(subString):
                    palidromes.append(subString)
                    backtrack(i + 1, palidromes)
                    palidromes.pop()
        backtrack(0, [])
        return res
        

        