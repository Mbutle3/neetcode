from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Use a special delimiter unlikely to appear in inputs
        return chr(31).join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(chr(31))
