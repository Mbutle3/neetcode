class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charMap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        res = []

        def backtrack(combo):
            if len(combo) == len(digits):
                res.append(combo.copy())
                return
            
            for char in charMap[digits[len(combo)]]:
                combo.append(char)
                backtrack(combo)
                combo.pop()
        backtrack([])
        return res
