class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for token in tokens:
            if token == '+':
                b, a = tokens.pop(), tokens.pop()
                res.append(int(a) + int(b))
            elif token == '-':
                b, a = tokens.pop(), tokens.pop()
                res.append(int(a) - int(b))
            elif token == '*':
                b, a = tokens.pop(), tokens.pop()
                res.append(int(a) * int(b))
            elif token == '/':
                b, a = tokens.pop(), tokens.pop()
                res.append(int(a) / int(b))
            else:
                res.append(token)
        return res[0]