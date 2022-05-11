from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []

        def traceback(idx, current):
            current.append(idx)

            if idx > 9:
                return 0

            if len(current) == k and sum(current) < n:
                return

            if sum(current) > n:
                return 0

            if len(current) == k:
                result.append(current[:])
                return 0

            for i in range(idx + 1, n):
                res = traceback(i, current)
                current.pop()

                if res == 0:
                    break

        for i in range(1, n):
            traceback(i, [])

        return result


if __name__ == "__main__":
    obj = Solution()

    k = 2
    n = 18
    assert obj.combinationSum3(k, n) == []

    k = 4
    n = 1
    assert obj.combinationSum3(k, n) == []

    k = 3
    n = 9
    assert obj.combinationSum3(k, n) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

    k = 3
    n = 7
    assert obj.combinationSum3(k, n) == [[1, 2, 4]]
