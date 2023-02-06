from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        p = list(range(len(graph)))

        def find(x):
            if x == p[x]:
                return x

            p[x] = find(p[x])
            return p[x]

        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)

            if parent_x != parent_y:
                p[parent_x] = parent_y

        for idx_node in range(len(graph)):
            nodes = graph[idx_node]
            for n in nodes:
                if find(idx_node) == find(n):
                    return False
                union(n, nodes[0])

        return True


if __name__ == "__main__":
    obj = Solution()

    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

    assert obj.isBipartite(graph) is False
