class Solution:

    def encode(self, strs: List[str]) -> str:
        words = []
        for word in strs:
            word_len = (str(len(word)))
            encoded_word =  word_len + '#' + word
            words.append(encoded_word)
        return ''.join(words)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            decoded_len = int(s[i : j])
            decoded_word = s[j + 1 : j + decoded_len]
            res.append(decoded_word)
            i = j + decoded_len 
        return res        
