import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        m = defaultdict(list)
        for u, v, w in times:
            m[u].append((v, w))

        visited = set()
        max_t = 0
        q = [(0, k)]

        while q:
            w, u = heapq.heappop(q)

            if u in visited:
                continue

            visited.add(u)
            max_t = max(max_t, w)

            for v1, w1 in m[u]:
                if v1 not in visited:
                    heapq.heappush(q, (w1 + w, v1))

        return max_t if len(visited) == n else -1


if __name__ == "__main__":
    obj = Solution()
    times = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]
    n = 3
    k = 1
    assert obj.networkDelayTime(times, n, k) == 2

    times = [[1, 2, 1], [2, 1, 3]]
    n = 2
    k = 2
    assert obj.networkDelayTime(times, n, k) == 3

    times = [[1, 2, 1]]
    n = 2
    k = 2
    assert obj.networkDelayTime(times, n, k) == -1

    times = [[1, 2, 1]]
    n = 2
    k = 1
    assert obj.networkDelayTime(times, n, k) == 1

    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    assert obj.networkDelayTime(times, n, k) == 2
