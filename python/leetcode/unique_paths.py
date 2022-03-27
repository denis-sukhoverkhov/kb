class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last_row = [1] * n

        for i in range(m-1):
            for j in range(n-2, -1, -1):
                last_row[j] += last_row[j+1]

        return last_row[0]


if __name__ == '__main__':
    obj = Solution()

    assert obj.uniquePaths(3, 7) == 28

    assert obj.uniquePaths(3, 2) == 3
