class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val == '+':
                stack.append(stack.pop() + stack.pop())
            elif val == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(b - a)
            elif val == '*':
                stack.append(stack.pop() * stack.pop())
            elif val == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append((Math.floor(b)) // a)
            else:
                stack.append(val)
        return stack[0]