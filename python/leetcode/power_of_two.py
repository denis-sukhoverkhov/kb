from math import log2, ceil, floor


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        res = log2(n)

        return ceil(res) == floor(res)


if __name__ == "__main__":
    obj = Solution()

    assert obj.isPowerOfTwo(-16) is False

    assert obj.isPowerOfTwo(8) is True

    assert obj.isPowerOfTwo(1) is True

    assert obj.isPowerOfTwo(2) is True

    assert obj.isPowerOfTwo(3) is False

    assert obj.isPowerOfTwo(16) is True
