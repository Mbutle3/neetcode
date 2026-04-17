class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        board.sort()
        ROWS = len(board)
        COLS = len(board)
        GRID = len(board)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                if val in ROWS[r] or val in COLS[c] or val in GRID[r //3, c//3]:
                    return False
                ROWS[r].append(val)
                COLS[c].append(val)
                GRID[r //3 , c//3].append(val)
        return True