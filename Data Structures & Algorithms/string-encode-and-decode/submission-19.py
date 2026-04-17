class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        n = len(strs)

        for word in strs:
            length = str(len(word))
            res.append(length + '#' + word)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 

        while i < len(s):
            j = i
            while s[j] != '#':
                j = j + 1
            length = int(s[i :  j  - 1])

            word = s[j + 1 : j + length ]
            res.append(word)
            
            i = j + 1 + length
        return res
        
