class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            encoded_length = str(len(word))
            encoded_word = encoded_length + '#' + word 
            res.append(encoded_word)
        return ''.join(encoded_word)

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            encoded_length = int(s[i : j])
            encoded_word = s[j + 1 : j + 1 + encoded_length]
            res.append(encoded_word)
            i = j + 1 + encoded_length
        return res

