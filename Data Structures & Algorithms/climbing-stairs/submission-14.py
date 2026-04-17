class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n - 1
        if n == 2:
            return n - 2
        return n + self.climbStairs(n - 1)
        
        