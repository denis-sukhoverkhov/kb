from copy import copy
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def traceback(start, current):

            current.append(start)

            if len(current) == k:
                result.append(copy(current))
                return

            for i in range(start+1, n+1,):
                traceback(i, current)
                current.pop()

        result = []

        for i in range(1, n + 1):
            traceback(i, [])

        return result


if __name__ == "__main__":
    obj = Solution()

    n = 4
    k = 2
    expected = [
        [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]
    ]
    assert obj.combine(n, k) == expected
