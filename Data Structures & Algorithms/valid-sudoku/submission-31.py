from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(list)
        COLS = defaultdict(list)
        GRID = defaultdict(list)
        seen = {}

        for r in board:
            for c in r:
                key = board[r][c]
                if key == '.':
                    continue
                if (key == ROWS[r] or key == COLS[c] or key == GRID[r][c]):
                    return False
                seen[key] = True
        return True
        