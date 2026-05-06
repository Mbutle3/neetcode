class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, i):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            if board[row][col] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            temp = board[row][col]
            board[row][col] = "#"

            res = (
                backtrack(row + 1, col, i + 1) or
                backtrack(row - 1, col, i + 1) or
                backtrack(row, col + 1, i + 1) or
                backtrack(row, col - 1, i + 1)
            )

            board[row][col] = temp
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        return False