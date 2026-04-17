class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            encoded_len = str(len(word))
            encoded_word = encoded_len + '#' + word
            res.append(encoded_word)
        return ''.join(res)
            

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            decoded_len = int(s[i : j])
            decoded_word = s[j + 1 : j + 1 + decoded_len]
            res.append(decoded_word)
            i = j + decoded_len + 1
        return res
