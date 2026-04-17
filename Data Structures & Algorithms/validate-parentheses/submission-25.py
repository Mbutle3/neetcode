class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_symbols = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in valid_symbols:
                if stack and stack[-1] == valid_symbols[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append()
        
        return len(stack) == 0
        