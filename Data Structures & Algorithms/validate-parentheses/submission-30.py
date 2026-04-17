class Solution:
    def isValid(self, s: str) -> bool:

        if s is None:
            return False

        valid_characters = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        stack = []

        for c in s:
            if c in valid_characters:
                if stack:
                    if valid_characters[c] == stack[-1]:
                        stack.pop()                
                    else:
                        stack.append(c)    
                else:
                    return False
        return len(stack) == 0
        