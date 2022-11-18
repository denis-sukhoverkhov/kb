from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        N = len(equations)

        for i in range(N):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1/values[i]

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1

            if y in graph[x]:
                return graph[x][y]

            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)

                    if temp == -1:
                        continue
                    else:
                        return temp * graph[x][i]

            return -1

        output = []

        for p, q in queries:
            output.append(dfs(p, q, set()))

        return output


if __name__ == "__main__":
    obj = Solution()

    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"],
               ["a", "e"], ["a", "a"],
               ["x", "x"]]
    assert obj.calcEquation(equations, values, queries) == \
           [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

