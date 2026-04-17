class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_words = []
        for word in strs:
            encoded_word = "#" + str(len(word)) + word
            encoded_words.append(encoded_word)
        return "".join(encoded_words)

    def decode(self, s: str) -> List[str]:
        l = 0
        i = 0
        n = len(s) - 1
        decoded_words = []
        while l < n:
            while s[i] != '#':
                i += 1
            decoded_len = str(s[i + 1])
            decoded_word = s[i : decoded_len]
            decoded_words.append(decoded_word)
            i = i + decoded_len + 1
            l = i + 1
        return decoded_words
