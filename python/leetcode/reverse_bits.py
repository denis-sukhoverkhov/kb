class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res


if __name__ == "__main__":
    obj = Solution()

    n = 0b11111111111111111111111111111101
    assert obj.reverseBits(n) == 3221225471

    n = 0b00000010100101000001111010011100
    assert obj.reverseBits(n) == 964176192
