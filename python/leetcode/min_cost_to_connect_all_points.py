import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        count_points = len(points)
        adj = {i: [] for i in range(count_points)}

        for i in range(count_points):
            x1, y1 = points[i]
            for j in range(i + 1, count_points):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append([cost, j])
                adj[j].append([cost, i])

        result = 0
        visited = set()
        min_heap = [[0, 0]]
        while len(visited) < count_points:
            cost, idx = heapq.heappop(min_heap)

            if idx in visited:
                continue

            result += cost
            visited.add(idx)

            for cost_nei, idx_nei in adj[idx]:
                if idx_nei in visited:
                    continue
                heapq.heappush(min_heap, [cost_nei, idx_nei])

        return result


if __name__ == "__main__":
    obj = Solution()

    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    assert obj.minCostConnectPoints(points) == 20
