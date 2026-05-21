class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word  # leaf marker

        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return
            nxt = node[ch]
            if "$" in nxt:
                res.add(nxt.pop("$"))  # collect + remove to avoid dupes

            board[r][c] = "#"
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = ch

            if not nxt:  # prune dead node
                del node[ch]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return list(res)