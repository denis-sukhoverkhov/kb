from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c_map = defaultdict(set)
        r_map = defaultdict(set)
        square_map = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in c_map[j] \
                            or board[i][j] in r_map[i] \
                            or board[i][j] in square_map[(i // 3, j // 3)]:
                        return False

                    c_map[j].add(board[i][j])
                    r_map[i].add(board[i][j])
                    square_map[(i // 3, j // 3)].add(board[i][j])

        return True


if __name__ == "__main__":
    obj = Solution()

    board = \
        [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert obj.isValidSudoku(board) is False

    board = \
        [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert obj.isValidSudoku(board)
