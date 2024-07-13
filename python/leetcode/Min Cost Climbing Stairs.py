from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])


if __name__ == "__main__":
    obj = Solution()

    cost = [10, 15, 20]
    assert obj.minCostClimbingStairs(cost) == 15

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert obj.minCostClimbingStairs(cost) == 6
