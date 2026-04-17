class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        print(f'ROWS: {ROWS}\nCols: {COLS}')
        return False        