from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        size = len(mat)

        if size % 2 != 0:
            skip_center = True
        else:
            skip_center = False

        summ = 0
        for i in range(size):
            summ += mat[i][i]

            j = size - 1 - i
            if i == j and skip_center:
                continue

            summ += mat[i][j]

        return summ


if __name__ == "__main__":
    obj = Solution()

    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    assert obj.diagonalSum(mat) == 8

    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    assert obj.diagonalSum(mat) == 25
