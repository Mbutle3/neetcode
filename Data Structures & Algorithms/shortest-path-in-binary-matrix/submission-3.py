class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        
        shortest_path = float('inf')

        def bfs(r,c):
            ROWS, COLS = len(grid), len(grid[0])

            visit = set()

            queue = deque()

            length = 0    
            
            queue.append((0,0))
            visit.add((0,0))

            while queue:

                for i in range(len(queue)):
                    r,c = queue.popleft()

                    if r == ROWS - 1 and c == COLS - 1:
                        return length
                    
                    neighbors = [
                        [1,0],
                        [0,1],
                        [-1,0],
                        [0,-1]
                    ]

                    for dr, dc in neighbors:
                        if((min(r + dr, c + dc) < 0) or r + dr == ROWS or c + dc == COLS or grid[r + dr][c + dc] == 1 or (r + dr, c + dc) in visit):
                            continue
                        
                        queue.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
                    length += 1
            return length
        
        for r in range(len(grid)):
            for c in range(len(grid[0])): 
                shortest_path = min(shortest_path, bfs(r,c))
        return shortest_path
