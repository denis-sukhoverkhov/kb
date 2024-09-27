class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        max_number = ''
        for i in range(len(number)):
            if number[i] == digit and i < len(number) - 1 and number[i+1] > digit:
                return number[0:i] + number[i+1:]
            elif number[i] == digit:
                curr_number = number[0:i] + number[i+1:]
                if curr_number > max_number:
                    max_number = curr_number

        return max_number


if __name__ == "__main__":
    obj = Solution()

    number = "8980"
    digit = "8"
    assert obj.removeDigit(number, digit) == '980'

    number = "123"
    digit = "3"
    assert obj.removeDigit(number, digit) == '12'

    number = "1231"
    digit = "1"
    assert obj.removeDigit(number, digit) == '231'

    number = "551"
    digit = "5"
    assert obj.removeDigit(number, digit) == '51'
