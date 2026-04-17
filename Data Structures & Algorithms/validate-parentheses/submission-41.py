class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for char in s:
            while stack:
                if char in valid_chars and char == valid_chars[char]:
                    stack.pop()
                else:
                    return False
            stack.append(char)
        return len(stack)
