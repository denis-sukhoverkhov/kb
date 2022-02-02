from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        summ_gas = sum(gas)
        summ_costs = sum(cost)

        if summ_gas < summ_costs:
            return -1

        idx_start = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                idx_start = i + 1

        return idx_start


if __name__ == "__main__":
    obj = Solution()

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert obj.canCompleteCircuit(gas=gas, cost=cost) == 3