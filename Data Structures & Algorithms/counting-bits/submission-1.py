class Solution:
    def countBits(self, n: int) -> List[int]:
        res =  bin(n).count('1')
        