from collections import defaultdict
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        count_roads_by_city = defaultdict(int)

        for r in roads:
            count_roads_by_city[r[0]] += 1
            count_roads_by_city[r[1]] += 1

        important_order = list(count_roads_by_city.items())
        important_order.sort(key=lambda o: -o[1])

        importances = [0] * n
        ct = n
        for o in important_order:
            importances[o[0]] = ct
            ct -= 1

        idx = 0
        while ct > 0:
            if importances[idx] == 0:
                importances[idx] = ct
                ct -= 1

            idx += 1

        res = 0
        for r in roads:
            res += importances[r[0]] + importances[r[1]]

        return res


if __name__ == "__main__":
    obj = Solution()

    roads = [[0, 1]]
    n = 5
    assert obj.maximumImportance(n, roads) == 9

    roads = [[0, 3], [2, 4], [1, 3]]
    n = 5
    assert obj.maximumImportance(n, roads) == 20

    n = 5
    roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    assert obj.maximumImportance(n, roads) == 43
