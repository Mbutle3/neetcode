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
        decodedArr = []
        while i < n:
            j = i
            if j < n and s[j] != '#':
                j += 1
            decodedLen = int(s[i : j])
            decodedWord = str(s[i + j : i +j + decodedLen])
            decodedArr.append(decodedWord)
            i = j + decodedLen + 1
        return decodedArr

