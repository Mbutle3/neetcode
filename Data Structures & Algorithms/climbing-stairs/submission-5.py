class Solution:
    def climbStairs(self, n: int) -> int:
        
        climb_stairs = 0 

        if n == 0:
            return 1

        if n == 1:
            return 1
        
        if n == 1:
            return 2

        climb_stairs = self.climb_stairs(n - 1) + self.climb_stairs(n - 2)
        return climb_stairs
