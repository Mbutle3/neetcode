class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True          # mark end of word

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and "#" in node

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    # --- helper ---
    def _find_node(self, prefix: str) -> dict | None:
        """Walk the trie along `prefix`, return the node or None if not found."""
        node = self.trie
        for char in prefix:
            if char not in node:
                return None
            node = node[char]
        return node