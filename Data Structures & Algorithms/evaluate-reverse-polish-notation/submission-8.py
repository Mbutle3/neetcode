class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for char in tokens:
            if char == '+':
                res = stack.pop() + stack.pop()
            elif char == '-':
                b = stack.pop()
                a = stack.pop()
                res = b - a
            elif char == '*':
                res = stack.pop() * stack.pop()
            elif char == '/':
                b = stack.pop()
                a = stack.pop()
                res = int(float(b) / a)
            else:
                stack.append(char)
        return res

        