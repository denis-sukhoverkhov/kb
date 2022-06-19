class Solution:
    def nthUglyNumber(self, n: int) -> int:

        dp = [1]

        p1 = 0
        p2 = 0
        p3 = 0
        for i in range(1, n):

            m1 = dp[p1] * 2
            m2 = dp[p2] * 3
            m3 = dp[p3] * 5

            dp.append(min(m1, m2, m3))

            if dp[i] == m1:
                p1 += 1
            if dp[i] == m2:
                p2 += 1
            if dp[i] == m3:
                p3 += 1

        return dp[n-1]


if __name__ == "__main__":
    obj = Solution()

    assert obj.nthUglyNumber(100) == 1536
    assert obj.nthUglyNumber(7) == 8
    assert obj.nthUglyNumber(4) == 4

    assert obj.nthUglyNumber(10) == 12
    assert obj.nthUglyNumber(1) == 1
