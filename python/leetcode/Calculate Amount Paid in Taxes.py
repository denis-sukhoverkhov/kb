from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        prev = 0

        res = 0
        payed = 0
        for i in range(len(brackets)):

            # if income <
            upper, percent = brackets[i]

            if income < upper:
                upper = income
            # payed = upper - prev
            payed = upper - prev
            res += payed * percent / 100
            prev = upper

        # r = (income - payed) * brackets[-1][1] / 100
        # res += r


        return res


if __name__ == "__main__":
    obj = Solution()

    brackets = [[3, 50], [7, 10], [12, 25]]
    income = 10
    assert obj.calculateTax(brackets, income) == 2.65
