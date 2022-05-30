from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        rows = len(graph)

        res = []

        def dfs(i, visited):

            visited.append(i)

            if i == rows - 1:
                res.append(visited.copy())
                return

            for j in graph[i]:
                dfs(j, visited)
                visited.pop()

        dfs(0, [])

        return res


if __name__ == "__main__":
    obj = Solution()

    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    assert obj.allPathsSourceTarget(graph) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4],
                                               [0, 1, 4]]
