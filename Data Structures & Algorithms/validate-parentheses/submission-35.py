class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = [] 

        seen = {}

        for char in s:
            if char in valid_chars and seen[char] == stack[0]:
                stack.pop()
            elif char in valid_chars:
                seen[char] = char
                stack.append(char)
            else:
                return False
        return len(stack) == 0