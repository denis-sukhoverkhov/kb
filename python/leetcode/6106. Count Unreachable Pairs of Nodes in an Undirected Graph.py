from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        m = {i: set() for i in range(n)}

        for x1, x2 in edges:
            m[x1].add(x2)
            m[x2].add(x1)

        was_counted = set()
        visited = set()

        def dfs(idx):
            nonlocal was_counted

            if idx in was_counted:
                return

            if idx in visited:
                return

            visited.add(idx)
            for node in m[idx]:
                dfs(node)

        res = []
        for i in range(n):
            visited = set()
            dfs(i)

            if len(visited):
                res.append(len(visited))
            was_counted = was_counted.union(visited)

        ans = 0

        prev = res[0]
        for i in range(1, len(res)):
            ans += prev * res[i]
            prev += res[i]
            # ans += res[i] * res[i + 1]
        return ans


if __name__ == "__main__":
    obj = Solution()
    n = 12
    edges = []
    assert obj.countPairs(n, edges) == 66

    n = 7
    edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
    assert obj.countPairs(n, edges) == 14

    n = 3
    edges = [[0, 1], [0, 2], [1, 2]]
    assert obj.countPairs(n, edges) == 0

