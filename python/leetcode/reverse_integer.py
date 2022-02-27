class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            tmp = x * -1
            sign = -1
        else:
            tmp = x
            sign = 1

        rev = 0
        while tmp:
            pop = tmp % 10
            tmp //= 10
            rev = rev * 10 + pop

        rev = rev * sign
        if (rev > 2**31 - 1) or rev < -2**31:
            return 0

        return rev


if __name__ == "__main__":
    obj = Solution()

    assert obj.reverse(120) == 21
    assert obj.reverse(-123) == -321
    assert obj.reverse(123) == 321
