from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def transpose(matrix):
            ln = len(matrix[0])
            for i in range(ln):
                for j in range(i, ln):
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp

        def reflect(matrix):
            ln = len(matrix[0])
            for i in range(ln):
                for j in range(ln // 2):
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[i][ln - j - 1]
                    matrix[i][ln - j - 1] = tmp

        transpose(matrix)
        reflect(matrix)


if __name__ == "__main__":
    obj = Solution()

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    obj.rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    obj.rotate(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
