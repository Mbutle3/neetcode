class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            encoded_length = str(len(word))
            encoded_word = encoded_length + '#' + word
            res.append(encoded_word)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0 
        n = len(s)
        res = []

        for i in range(n):
            j = i
            while s[j] != '#':
                j += 1
            decoded_length = int(s[i : j])
            decoded_word = str(s[j + 1 : j + 1 : decoded_length])
            res.append(decoded_word)
            i = j + 1 + decoded_length
        return res


        
