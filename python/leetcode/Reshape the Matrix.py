from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        rows = len(mat)
        columns = len(mat[0])

        if rows * columns != r * c:
            return mat

        result = [[0] * c for _ in range(r)]
        ii, jj = 0, 0
        for i in range(rows):
            for j in range(columns):
                result[ii][jj] = mat[i][j]

                jj += 1
                if jj >= c:
                    jj = 0
                    ii += 1

        return result


if __name__ == "__main__":
    obj = Solution()

    mat = [[1, 2, 3, 4]]
    r = 2
    c = 2
    assert obj.matrixReshape(mat, r, c) == [[1, 2], [3, 4]]

    mat = [[1, 2], [3, 4]]
    r = 2
    c = 4
    assert obj.matrixReshape(mat, r, c) == [[1, 2], [3, 4]]

    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    assert obj.matrixReshape(mat, r, c) == [[1, 2, 3, 4]]
