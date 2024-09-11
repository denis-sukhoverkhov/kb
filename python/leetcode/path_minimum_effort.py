import heapq
from cmath import inf
from typing import List


class Solution:

    def __init__(self):
        self.min_heap = [(0, 0, 0)]

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        columns = len(heights[0])

        efforts = [[None] * columns for i in range(rows)]

        while self.min_heap:
            effort, i, j = heapq.heappop(self.min_heap)

            if i == rows - 1 and j == columns - 1:
                return effort

            node_left = self.get_new_node(i, j - 1, heights, effort, i, j)
            self.add_node_if_it_needs(node_left, efforts)

            node_right = self.get_new_node(i, j + 1, heights, effort, i, j)
            self.add_node_if_it_needs(node_right, efforts)

            node_top = self.get_new_node(i - 1, j, heights, effort, i, j)
            self.add_node_if_it_needs(node_top, efforts)

            node_bottom = self.get_new_node(i + 1, j, heights, effort, i, j)
            self.add_node_if_it_needs(node_bottom, efforts)

    def add_node_if_it_needs(self, new_node, efforts):
        if not new_node:
            return

        effort, i, j = new_node

        if efforts[i][j] is not None and efforts[i][j] <= effort:
            return

        heapq.heappush(self.min_heap, new_node)
        efforts[i][j] = effort

    def get_new_node(self, i, j, heights, current_effort, current_i, curent_j):
        if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]):
            return None

        return (
            max(current_effort, abs(heights[i][j] - heights[current_i][curent_j])), i, j)


if __name__ == "__main__":
    obj = Solution()

    heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    assert obj.minimumEffortPath(heights) == 0

    obj = Solution()
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    assert obj.minimumEffortPath(heights) == 1

    obj = Solution()
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    assert obj.minimumEffortPath(heights) == 2
