from typing import List


class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            for zero in range(m, zeros - 1, -1):
                for one in range(n, ones - 1, -1):
                    dp[zero][one] = max(dp[zero - zeros][one - ones] + 1, dp[zero][one])

        return dp[m][n]


if __name__ == "__main__":
    obj = Solution()

    # strs = ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0110101",
    #  "0", "11", "01", "00", "01111", "0011", "1", "1000", "0", "11101", "1", "0", "10", "0111"]
    # m = 9
    # n = 80
    # assert obj.findMaxForm(strs, m, n) == 17

    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    assert obj.findMaxForm(strs, m, n) == 4

    strs = ["10", "0001", "111001", "1", "0"]
    m = 4
    n = 3
    assert obj.findMaxForm(strs, m, n) == 3

    strs = ["10", "0", "1"]
    m = 1
    n = 1
    assert obj.findMaxForm(strs, m, n) == 2

