class Solution:
    def countBits(self, n: int) -> List[int]:
        return sum(bin(n).count('1'))