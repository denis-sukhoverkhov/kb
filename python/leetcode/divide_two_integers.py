class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        bits_in_integer_number = 31
        tmp = 0
        quotient = 0
        max_value_by_description = 2147483647

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        for i in range(bits_in_integer_number, -1, -1):
            if tmp + (divisor << i) <= dividend:
                tmp += (divisor << i)
                quotient |= 1 << i

        if sign == -1:
            quotient = -quotient

        return min(max_value_by_description, quotient)


if __name__ == "__main__":
    obj = Solution()

    assert obj.divide(-2147483648, -1) == 2147483647
    assert obj.divide(1, 1) == 1
    assert obj.divide(10, 3) == 3
    assert obj.divide(7, -3) == -2
    assert obj.divide(0, 1) == 0
