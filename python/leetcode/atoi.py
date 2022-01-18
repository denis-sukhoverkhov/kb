class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        result = 0
        sign = 1
        sign_was_set = False
        first_digit_was_set = False
        for i in s:
            if sign_was_set and i in '+-':
                break

            if first_digit_was_set and i in '+-':
                break

            if i.isdigit():
                first_digit_was_set = True
                result = result * 10 + int(i)
            elif i == '-':
                sign = -1
                sign_was_set = True
            elif i == '+':
                sign_was_set = True
            else:
                break
        result = result * sign
        if result < -2**31:
            return -2**31
        elif result > (2**31 - 1):
            return 2**31 - 1
        else:
            return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.myAtoi("00000-42a1234") == 0

    assert obj.myAtoi("+-12") == 0

    assert obj.myAtoi("+1") == 1

    assert obj.myAtoi("0032") == 32

    assert obj.myAtoi("4193 with words") == 4193

    assert obj.myAtoi("   -42") == -42

    assert obj.myAtoi("42") == 42
