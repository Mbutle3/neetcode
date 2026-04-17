class Solution:

    def encode(self, strs: List[str]) -> str:
        words = []
        for word in strs:
            word_len = (str(len(word)))
            encoded_word =  '#' + word_len + word
            words.append(encoded_word)
        return ''.join(encoded_word)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            decoded_len = int(s[j + 1])
            decoded_word = s[j + 1 : decoded_len] + 1
            res.append(decoded_word)
            i = j + decoded_len + 1
        return res        
