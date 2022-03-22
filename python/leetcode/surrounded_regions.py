from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def bfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O':
                return

            board[r][c] = 'T'

            bfs(r-1, c)
            bfs(r + 1, c)
            bfs(r, c - 1)
            bfs(r, c + 1)

        for i in range(rows):
            for j in range(cols):
                if i in (0, rows-1) or j in (0, cols-1):
                    bfs(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'


if __name__ == "__main__":
    obj = Solution()

    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    obj.solve(board)

    assert board == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"],
                     ["X", "O", "X", "X"]]
