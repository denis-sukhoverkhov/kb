from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:

        maxv, minv = salary[0], salary[0]
        for i in salary:
            maxv = max(maxv, i)
            minv = min(minv, i)

        summ = []
        for i in salary:
            if i not in (maxv, minv):
                summ.append(i)

        return sum(summ) / len(summ) if summ else 0
