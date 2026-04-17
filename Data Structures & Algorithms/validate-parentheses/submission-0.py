class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        valid_characters={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for char in s:
            if char in valid_characters:
                if stack:
                    top_element = stack.pop()
                if valid_characters[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
                
        