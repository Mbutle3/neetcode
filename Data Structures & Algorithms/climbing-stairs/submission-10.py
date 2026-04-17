class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n)
        
        