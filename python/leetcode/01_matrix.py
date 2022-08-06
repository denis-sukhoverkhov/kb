from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        columns = len(mat[0])
        q = []

        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = '#'

        for i, j in q:
            for k, l in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= k < rows and 0 <= l < columns and mat[k][l] == '#':
                    mat[k][l] = mat[i][j] + 1
                    q.append((k, l))

        return mat


if __name__ == "__main__":
    obj = Solution()

    mat = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
           [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
           [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
           [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
           [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
           [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
           [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]

    expected = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
                [1, 0, 0, 0, 1, 2, 1, 1, 0, 1],
                [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
                [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]]

    err = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
           [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
           [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
           [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
           [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
           [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
           [1, 0, 0, 0, 1, 2, 1, 1, 0, 1],
           [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
           [2, 2, 2, 1, 0, 1, 0, 0, 1, 1]]
    assert obj.updateMatrix(mat) == expected

    mat = [[0, 0, 0],
           [0, 1, 0],
           [1, 1, 1]]
    assert obj.updateMatrix(mat) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert obj.updateMatrix(mat) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]