from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        columns = set()
        rows = set()
        negative_diagonal = set()
        positive_diagonal = set()

        board = [['.'] * n for _ in range(n)]

        def traceback(r):
            if r >= n:
                res.append(
                    [''.join(i) for i in board]
                )
                return

            for c in range(n):
                if r in rows or c in columns or r + c in positive_diagonal or r - c in negative_diagonal:
                    continue

                columns.add(c)
                rows.add(r)
                positive_diagonal.add(r+c)
                negative_diagonal.add(r-c)
                board[r][c] = 'Q'

                traceback(r+1)

                columns.remove(c)
                rows.remove(r)
                positive_diagonal.remove(r + c)
                negative_diagonal.remove(r - c)
                board[r][c] = '.'

        traceback(0)

        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.solveNQueens(4) == [[".Q..", "...Q", "Q...", "..Q."],
                                   ["..Q.", "Q...", "...Q", ".Q.."]]
