class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        summation, i = 0, 0
        if divisor > dividend > 0:
            return 0
        elif divisor < dividend < 0:
            return 0
        elif divisor == 1:
            return dividend
        elif divisor == -1:
            return -dividend

        if divisor > 0 and dividend > 0:
            while summation <= dividend:
                summation += divisor
                i += 1
            return i - 1
        elif divisor < 0 and dividend > 0:
            while summation <= dividend:
                summation += abs(divisor)
                i += 1
            return -i + 1
        elif divisor < 0 and dividend < 0:
            while summation >= dividend:
                summation += divisor
                i += 1
            return i - 1
        elif divisor > 0 and dividend < 0:
            while summation <= abs(dividend):
                summation += abs(divisor)
                i += 1
            return -i + 1
        else:
            return 0