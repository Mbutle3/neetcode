class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        n = len(strs)
        for i in range (n):
            encoded_length = str(len(strs[i]))
            encoded_word = encoded_length + "#" + strs[i]
            res.append(encoded_word)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s) 

        for i in range(n):
            j = i 
            while s[j] != '#':
                j += 1
            decoded_length = int(s[i : j + 1])
            decoded_word = s[j + 1 : decoded_length + j + 1]
            res.append(decoded_word)
            i = decoded_length + j + 1
        return res
