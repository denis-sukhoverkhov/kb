from typing import List


class Solution:
    # def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    #
    #     rows = len(matrix)
    #     columns = len(matrix[0])
    #
    #     if rows < columns:
    #         diff = columns - rows
    #         matrix += [[0] * columns for _ in range(diff)]
    #
    #     if columns < rows:
    #         diff = abs(columns - rows)
    #         for i in range(rows):
    #             matrix[i] += [0]*diff
    #
    #     for i in range(len(matrix)):
    #         for j in range(i, len(matrix[0])):
    #             tmp = matrix[i][j]
    #             matrix[i][j] = matrix[j][i]
    #             matrix[j][i] = tmp
    #
    #     if columns > rows:
    #         diff = columns - rows
    #         for i in range(len(matrix)):
    #             matrix[i] = matrix[i][:-diff]
    #
    #     if columns < rows:
    #         diff = abs(columns - rows)
    #         for i in range(len(matrix)-diff, len(matrix)):
    #             del matrix[-1]
    #
    #     return matrix

    # class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]

        return ans


if __name__ == "__main__":
    obj = Solution()

    matrix = [[2], [6], [2]]
    assert obj.transpose(matrix) == [[2, 6, 2]]

    matrix = [[1, 4], [2, 5], [3, 6]]
    assert obj.transpose(matrix) == [[1, 2, 3], [4, 5, 6]]

    matrix = [[1, 2, 3], [4, 5, 6]]
    assert obj.transpose(matrix) == [[1, 4], [2, 5], [3, 6]]

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert obj.transpose(matrix) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
