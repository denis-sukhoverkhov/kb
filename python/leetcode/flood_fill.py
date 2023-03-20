from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])
        color_for_change = image[sr][sc]

        def dfs(i, j):

            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1:
                return

            if image[i][j] != color_for_change or color_for_change == newColor:
                return

            image[i][j] = newColor

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        dfs(sr, sc,)

        return image


if __name__ == "__main__":
    obj = Solution()

    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    newColor = 1
    assert obj.floodFill(image, sr, sc, newColor) == [[0, 0, 0], [0, 1, 1]]

    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    assert obj.floodFill(image, sr, sc, newColor) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    assert obj.floodFill(image, sr, sc, newColor) == [[2, 2, 2], [2, 2, 2]]
