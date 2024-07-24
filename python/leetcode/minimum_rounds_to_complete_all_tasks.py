from collections import defaultdict
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        m = defaultdict(int)

        for t in tasks:
            m[t] += 1

        min_rounds = 0
        for _, v in m.items():
            if v == 1:
                return -1

            curr_res = v // 3
            least = v % 3

            if least == 1:
                min_rounds += curr_res - 1 + 2
            elif least == 2:
                min_rounds += 1 + curr_res
            else:
                min_rounds += curr_res

        return min_rounds


if __name__ == "__main__":
    obj = Solution()

    tasks = [66, 66, 63, 61, 63, 63, 64, 66, 66, 65, 66, 65, 61, 67, 68, 66, 62, 67, 61, 64, 66, 60,
             69, 66, 65, 68, 63, 60, 67, 62, 68, 60, 66, 64, 60, 60, 60, 62, 66, 64, 63, 65, 60, 69,
             63, 68, 68, 69, 68, 61]
    assert obj.minimumRounds(tasks) == 20

    tasks = [5, 5, 5, 5]
    assert obj.minimumRounds(tasks) == 2

    tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    assert obj.minimumRounds(tasks) == 4
