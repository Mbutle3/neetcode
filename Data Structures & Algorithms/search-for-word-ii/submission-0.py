class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores the complete word at leaf

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        ROWS, COLS = len(board), len(board[0])
        results = set()

        def dfs(r, c, node):
            ch = board[r][c]

            # Prune: char not in trie path
            if ch not in node.children:
                return

            next_node = node.children[ch]

            # Found a word
            if next_node.word:
                results.add(next_node.word)
                next_node.word = None  # avoid duplicates

            # Mark visited
            board[r][c] = '#'

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    dfs(nr, nc, next_node)

            # Restore
            board[r][c] = ch

            # Trie pruning: remove dead-end nodes
            if not next_node.children:
                del node.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return list(results)