import random
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        while True:
            guessed_num = random.randint(1, n)
            guess = guess(guessed_num)
            if  guess == 0:
                break
            elif guess == -1:
                print('guessed too high')
            else:
                print('guessed too low')
        
        return guessed_num

