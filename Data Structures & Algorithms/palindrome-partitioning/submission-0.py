class Solution:
    
    def isPalidrome(self, s) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        palis = []
        

        def backtrack(i, palis):
            if i == len(s):
                res.append(palis.copy())
                return
            
            for j in range(i, len(s)):
                substring = s[i : j + 1]
                if self.isPalidrome(substring):
                    palis.append(substring)
                    backtrack(j + 1, palis)
                    palis.pop()
        backtrack(0, [])
        return res