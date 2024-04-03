# 79. Word Search
# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()

        def backtrack(i, j, k):
            if k >= len(word):
                return True
            
            if  i < 0 or  i >= len(board) or j < 0 or j >= len(board[0]):
                return False
        
            if board[i][j] != word[k]:
                return False
            
            key = (i, j)

            if key in visited:
                return False
            visited.add(key)
            
            res = backtrack(i-1, j, k+1) or backtrack(i+1, j, k+1) or backtrack(i, j -1 , k+1) or backtrack(i, j+1, k+1)

            visited.remove(key)

            return res

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        
        return False


if __name__ == "__main__":
    obj = Solution()

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    res = obj.exist(board, word)
    assert res, "actual: %s" % res