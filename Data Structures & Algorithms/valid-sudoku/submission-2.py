class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #Get ROWS and COLS
        ROWS = len(board)
        COLS = len(board[0])
        print(f'ROWS: {ROWS}\nCols: {COLS}')

        subgrid = {}
        seen_rows = set()
        seen_cols = set()
        
        for r in ROWS:
            for c in COLS:
                if board[r][c] not in subgrid:
                    if r not in seen_rows and c not in seen_cols:
                        subgrid[r][c] = True
                    else:
                        return False
                seen_rows.add(r)
                seen_rows.add(c)
        return True      