from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        response = 0
        prev = values[0]
        for i in range(1, len(values)):
            response = max(values[i] - i + prev, response)
            prev = max(prev, values[i] + i)

        return response


if __name__ == "__main__":
    obj = Solution()

    values = [8, 1, 5, 2, 6]
    assert obj.maxScoreSightseeingPair(values) == 11
