class Solution:
    def isValid(self, s: str) -> bool:
        
        valid_chars = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for char in s:
            if char not in valid_chars:
                return False
            elif stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0