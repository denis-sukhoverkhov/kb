import sys


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum2(self, A):

        return self.util(A, len(A) - 1, len(A[0]) - 1)

    def util(self, A, m, n):
        if m < 0 or n < 0:
            return sys.maxsize
        elif m == 0 and n == 0:
            return A[m][n]
        else:
            return A[m][n] + min(self.util(A, m - 1, n), self.util(A, m, n - 1))

    def minPathSum(self, A):

        rows = len(A)
        columns = len(A[0])

        res = [[0] * columns for _ in range(rows)]
        res[0][0] = A[0][0]
        for i in range(1, columns):
            res[0][i] = res[0][i-1] + A[0][i]

        for i in range(1, rows):
            res[i][0] = res[i-1][0] + A[i][0]

        for i in range(1, rows):
            for j in range(1, columns):
                res[i][j] = min(A[i][j] + res[i][j - 1], A[i][j] + res[i-1][j])

        return res[rows-1][columns-1]

if __name__ == "__main__":
    s = Solution()

    A = [[1, 3, 2, ],
         [4, 3, 1, ],
         [5, 6, 1, ], ]

    res = s.minPathSum(A)
    assert res == 8
