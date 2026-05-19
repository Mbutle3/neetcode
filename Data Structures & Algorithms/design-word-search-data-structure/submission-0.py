class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True  # mark end-of-word after loop

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.trie)

    def _dfs(self, word: str, i: int, node: dict) -> bool:
        if i == len(word):
            return '#' in node  # valid only if we're at a terminal

        char = word[i]

        if char == '.':
            # try every child branch
            for key in node:
                if key != '#' and self._dfs(word, i + 1, node[key]):
                    return True
            return False
        else:
            if char not in node:
                return False
            return self._dfs(word, i + 1, node[char])