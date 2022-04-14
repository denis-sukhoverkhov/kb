from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        2 - died
        3 - born
        """

        rows = len(board)
        columns = len(board[0])

        for i in range(rows):
            for j in range(columns):
                neigbors = self.get_count_live_neighbors(
                    board=board, row=i, col=j, max_rows=rows, max_cols=columns)

                if neigbors < 2 and board[i][j] == 1:
                    board[i][j] = 2
                elif board[i][j] == 1 and neigbors > 3:
                    board[i][j] = 2
                elif board[i][j] == 0 and neigbors == 3:
                    board[i][j] = 3

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1

        pass

    def get_count_live_neighbors(self, board, row, col, max_rows, max_cols):
        neigbors = 0

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if max_rows > i >= 0 and max_cols > j >= 0 and (row != i or col != j) \
                        and board[i][j] in (1, 2):
                    neigbors += 1

        return neigbors


if __name__ == "__main__":
    obj = Solution()

    board = [[1, 1], [1, 0]]
    obj.gameOfLife(board)
    assert board == [[1, 1], [1, 1]]

    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    obj.gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
