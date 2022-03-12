from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_row = False

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0

                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        zero_row = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(0, rows):
                matrix[i][0] = 0

        if zero_row:
            for j in range(0, cols):
                matrix[0][j] = 0


if __name__ == "__main__":
    obj = Solution()

    matrix = [[1, 0, 3]]
    obj.setZeroes(matrix)
    assert matrix == [[0, 0, 0]]


    matrix = [[1], [0], [3]]
    obj.setZeroes(matrix)
    assert matrix == [[0], [0], [0]]

    matrix = [[1, 0]]
    obj.setZeroes(matrix)
    assert matrix == [[0, 0]]

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    obj.setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
