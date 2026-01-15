class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        a, b = abs(dividend), abs(divisor)
        quotient = 0

        while a >= b:
            temp_divisor = b
            multiple = 1
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            a -= temp_divisor
            quotient += multiple

        result = -quotient if negative else quotient

        return max(INT_MIN, min(INT_MAX, result))