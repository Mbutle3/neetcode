class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            length = str(len(word))
            res.append(length + '#' + word)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            word = s[i + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res