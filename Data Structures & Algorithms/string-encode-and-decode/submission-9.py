class Solution:

    def encode(self, strs: List[str]) -> str:
        
        n = len(strs)
        res = []
        for c in strs:
            res.append(str(len(c)) + "#" + c)
        return ''.join(res)




    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        curr_str = ""
        j = 0
        for i in range(n):
            j = i
            while s[i] != '#':
                j += 1
            else:
                curr_str += s[j]
            res.append(curr_str)
            curr_str = ""
        return res
            
