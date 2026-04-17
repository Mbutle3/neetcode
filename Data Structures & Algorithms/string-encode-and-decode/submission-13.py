class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        n = len(strs)
        for i in range(n):
            res.append(len(str(i)) + '#' + strs[i])
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        curr_string = ''
        for i in range(s):
            while s[i] != '#':
                curr_string += s[i]
            i = len(s) + 1
            res.append(curr_string)
        return res
                
