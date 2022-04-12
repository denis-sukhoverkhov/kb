class Solution:
    def largestInteger(self, num: int) -> int:

        num_str = str(num)

        even_digits = []
        odd_digits = []
        for i in num_str:
            digit = int(i)

            if digit % 2 == 0:
                even_digits.append(digit)
            else:
                odd_digits.append(digit)

        even_digits.sort()
        odd_digits.sort()

        result = 0
        for i in num_str:
            digit = int(i)

            result *= 10
            if digit % 2 == 0:
                result += even_digits.pop()
            else:
                result += odd_digits.pop()

        return result


if __name__ == "__main__":
    obj = Solution()
    assert obj.largestInteger(1234) == 3412

    assert obj.largestInteger(65875) == 87655
