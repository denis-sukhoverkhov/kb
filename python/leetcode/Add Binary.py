class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff_len = abs(len(a) - len(b))
        if len(a) > len(b):
            b = ('0' * diff_len) + b
        else:
            a = ('0' * diff_len) + a

        res = []
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            b1 = int(a[i], 2)
            b2 = int(b[i], 2)
            res.append(str(b1 ^ b2 ^ carry))
            carry = (b1 & b2) | (b1 & carry) | (b2 & carry)

        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])


if __name__ == "__main__":
    obj = Solution()

    a = "11"
    b = "1"
    assert obj.addBinary(a, b) == "100"

    assert obj.addBinary("1010",
                         "1011") \
           == "10101"