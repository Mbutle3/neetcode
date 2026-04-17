class Solution:
    def isValid(self, s: str) -> bool:

        valid_char = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for c in s:
            if c in valid_char:
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        