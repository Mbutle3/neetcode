class Solution:
    def isValid(self, s: str) -> bool:

        valid_chars = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        stack = []

        for char in s:
            if char in valid_chars:
                char_compliment = valid_chars[char]
                if stack:
                    if stack[-1] == char_compliment:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(char)
        return len(stack) == 0

