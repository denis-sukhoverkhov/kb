from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            matrix[i].append('0')
        matrix.append(['0']*len(matrix[0]))

        dp = [int(matrix[-1][i]) for i in range(len(matrix[-1]))]

        mx = 0
        for r in range(len(matrix) - 1, -1, -1):
            new_row = dp.copy()
            for c in range(len(matrix[0]) - 2, -1, -1):

                if int(matrix[r][c]) == 0:
                    new_row[c] = 0
                else:
                    new_row[c] = 1 + min(new_row[c+1], dp[c], dp[c + 1])
                    mx = max(mx, new_row[c])
            dp = new_row
        return mx**2


if __name__ == "__main__":
    obj = Solution()

    matrix = [["1", "1"], ["1", "1"]]
    assert obj.maximalSquare(matrix) == 4

    matrix = [["1"]]
    assert obj.maximalSquare(matrix) == 1

    matrix = [["0"]]
    assert obj.maximalSquare(matrix) == 0

    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    assert obj.maximalSquare(matrix) == 4

    matrix = [["1", "0", "1", "0", "0"],
              ["1", "1", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "1", "1", "1"]]
    assert obj.maximalSquare(matrix) == 9

    matrix = [["0", "1"], ["1", "0"]]
    assert obj.maximalSquare(matrix) == 1

