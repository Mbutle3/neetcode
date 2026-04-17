from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Result list to store the count of 1's for each number from 0 to n
        res = []
        
        # Iterate from 0 to n
        for i in range(n ):
            # Count the number of 1's in the binary representation of i
            res.append(bin(i).count('1'))
        
        return res
