from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

        dp1 = [1] * len(ratings)
        dp2 = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                dp1[i] = dp1[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                dp2[i] = dp2[i+1] + 1

        res = 0
        for i in range(len(dp1)):
            res += max(dp1[i], dp2[i])

        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.candy([1, 6, 10, 8, 7, 3, 2]) == 18
    # 1 2 3 1 1 1 1
    # 1 1 5 4 3 2 1

    assert obj.candy([1, 2, 3, 1, 0]) == 9
    assert obj.candy([1, 3, 2, 2, 1]) == 7
