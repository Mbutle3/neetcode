class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(bin(n))