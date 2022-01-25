class Solution:
    def climbStairs(self, n: int) -> int:
        row = [0] * (n - 1) + [1, 1]

        for i in range(len(row)-3, -1, -1):
            row[i] = row[i+1] + row[i+2]

        return row[0]


if __name__ == "__main__":
    obj = Solution()

    assert obj.climbStairs(5) == 8

    assert obj.climbStairs(3) == 3

    assert obj.climbStairs(2) == 2
