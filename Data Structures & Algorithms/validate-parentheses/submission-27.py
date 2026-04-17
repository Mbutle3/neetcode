class Solution:
    def isValid(self, s: str) -> bool:
        valid_characters = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        stack = []

        for c in s:
            if c in valid_characters:
                if stack and valid_characters[c] == stack[-1]:
                    stack.append(c)
                else:
                    stack.pop()
            else:
                return False
        return len(stack) == 0
        