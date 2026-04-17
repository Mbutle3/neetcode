class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        visit = set()
        def dfs(grid, r, v, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r,v) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 1):
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
        number_of_islands += dfs(grid, r + 1, c, visit) 
        number_of_islands += dfs(grid, r - 1, c, visit)
        number_of_islands += dfs(grid, r, c + 1, visit)
        number_of_islands += dfs(grid, r, c - 1, visit)
        visit.remove((r,c))
        return number_of_islands