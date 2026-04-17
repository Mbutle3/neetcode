class Solution:
    def climbStairs(self, n: int) -> int:
        stairs_climbed = 0
        if n == 1:
            stairs_climbed += 1
            return stairs_climbed
        if n == 2:
            stairs_climbed += 2
            return stairs_climbed
        stairs_climbed = self.climbStairs(n-1) 

        return stairs_climbed
