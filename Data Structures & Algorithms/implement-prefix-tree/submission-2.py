class PrefixTree:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True 

        
    def _find_node(self, word: str) -> dict | None:
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return node
        

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and "#" in node
        

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None
        
        