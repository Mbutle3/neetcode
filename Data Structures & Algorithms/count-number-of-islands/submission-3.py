class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #1. create directions that we can traverse the grid in (up, down, right, left)
        directions = [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]

        #2. create constants to maintain the len the row & col of the grid (M * N) 
        ROWS = len(grid)
        COLS = len(grid[0])

        #3. create a pointer to store islands found
        islands = 0

        #4. declare dfs helper method that takes in the current row and col
        def dfs(row, col):
            # 5. if we are still in a valid point 
            #    -> row & col isn't out of bounds 
            #    -> 
            if (ROWS <= row < 0 or COLS <= col < 0  or grid[row][col] == "0"):
                return
            
            grid[row][col] = "0"

            for dr, dc in directions:
                dfs(row + dr, col + dc)
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands