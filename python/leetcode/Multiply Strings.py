class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0": return "0"

        num1, num2 = (num2, num1) if len(num2) > len(num1) else (num1, num2)

        res = 0
        for i in range(len(num2) - 1, -1, -1):
            digit1 = num2[i]

            tmp = 0
            mem = 0
            for j in range(len(num1) - 1, -1, -1):
                digit2 = num1[j]
                product = int(digit1) * int(digit2)
                least = product % 10
                tmp += 10 ** (len(num1) - 1 - j) * (least + mem)
                mem = product // 10
            if mem:
                tmp += mem * 10 ** len(num1)
            res += tmp * (10 ** (len(num2) - 1 - i))

        return str(res)


if __name__ == "__main__":
    obj = Solution()

    assert obj.multiply("12", "367") == "4404"
    assert obj.multiply("123", "456") == "56088"
    assert obj.multiply("1234", "100") == "123400"
    assert obj.multiply("9", "9") == "81"
