class Solution:
    def tribonacci(self, n: int) -> int:

        fibo = [0, 1, 1]
        for i in range(3, n+1):
            fibo.append(
                fibo[i-3] + fibo[i-2] + fibo[i - 1]
            )

        return fibo[n]


if __name__ == "__main__":
    obj = Solution()

    assert obj.tribonacci(4) == 4
