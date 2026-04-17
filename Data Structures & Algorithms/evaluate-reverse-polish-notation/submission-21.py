class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr = tokens
        res = []
        while curr:
            if curr == '+':
                res.append(float(curr.pop()) + float(curr.pop()))
            elif curr == '-':
                b = curr.pop()
                a = curr.pop()
                res.append(float(b) - float(a))
            elif curr == '*':
                res.append(float(curr.pop()) * float(curr.pop()))
            elif curr == '/':
                b = curr.pop()
                a = curr.pop()
                res.append(float(b) // float(a))
            else:
                res.append(curr)
        return res[0]


        

        