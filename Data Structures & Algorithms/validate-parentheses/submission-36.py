class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = [] 

        for char in s:
            if char in valid_chars:
                if stack and valid_chars[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
