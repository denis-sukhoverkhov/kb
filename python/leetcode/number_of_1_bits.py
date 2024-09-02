class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += 1
            n &= (n - 1)

        return res


if __name__ == "__main__":
    obj = Solution()

    n = 0b0000000000000000000000000001011
    assert obj.hammingWeight(n) == 3
