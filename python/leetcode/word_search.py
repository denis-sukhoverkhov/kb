from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        path = set()

        def traceback(i, j, k):
            if k == len(word):
                return True

            if i < 0 or j < 0 or i > rows - 1 or j > cols - 1 or board[i][j] != word[k] or (
            i, j) in path:
                return False

            path.add((i, j))

            res = (traceback(i + 1, j, k + 1)
                   or traceback(i - 1, j, k + 1)
                   or traceback(i, j + 1, k + 1)
                   or traceback(i, j - 1, k + 1)
                   )

            path.remove((i, j))

            return res

        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                res = traceback(i, j, 0)
                if res:
                    return True

        return False


if __name__ == "__main__":
    obj = Solution()

    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    assert obj.exist(board, word) is True

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    assert obj.exist(board, word) is True
