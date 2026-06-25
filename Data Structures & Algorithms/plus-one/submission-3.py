class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        #1. walk backwards though digits
        for i in range(len(digits) - 1, -1, -1):
            # 2. if the last digit is less than 9 inc by 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            #3. otherwise overwrite the last digit to be a 0 
            #   and then append a 1 to the digits arr
            digits[i] = 0
        return [1] + digits
