class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:  # mid is too high
                high = mid - 1
            else:  # mid is too low
                low = mid + 1
        return -1  # shouldn't be reached given problem guarantees