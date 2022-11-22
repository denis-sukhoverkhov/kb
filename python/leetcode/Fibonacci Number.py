class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]

        for i in range(2, n + 1):
            f.append(
                f[i - 2] + f[i - 1]
            )

        return f[n]


if __name__ == "__main__":
    obj = Solution()

    assert obj.fib(2) == 1
    assert obj.fib(3) == 2
    assert obj.fib(4) == 3
