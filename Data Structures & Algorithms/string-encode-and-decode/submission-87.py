class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedArr = []
        for word in strs:
            encodedWord = '#' + str(len(word)) + word
            encodedArr.append(encodedWord)
        return ''.join(encodedArr)




    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        decodedArr = []
        while i < (n):
            while i < n and s[i] != '#':
                i += 1
            i += 1
            decodedLen = int(s[i])
            decodedWord = str(s[i + 1 : decodedLen + i + 1])
            decodedArr.append(decodedWord)
            i = decodedLen + 1
        return decodedArr







        return ['empty']
