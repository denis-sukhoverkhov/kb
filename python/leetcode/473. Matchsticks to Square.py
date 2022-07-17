from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        l = len(matchsticks)
        if l < 4:
            return False

        summ = sum(matchsticks)
        ln = summ / 4

        if ln != summ // 4:
            return False

        sq = [0] * 4

        matchsticks.sort(reverse=True)

        def traceback(i):
            if i == l:
                return True

            for j in range(4):
                if matchsticks[i] + sq[j] <= ln:
                    sq[j] += matchsticks[i]
                    res = traceback(i+1)
                    if traceback(i+1):
                        return True
                    sq[j] -= matchsticks[i]

            return False

        return traceback(0)


if __name__ == "__main__":
    obj = Solution()

    assert obj.makesquare([1, 1, 2, 2, 2]) is True
    assert obj.makesquare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) is True
    assert obj.makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]) is True
    assert obj.makesquare([3, 3, 3, 3, 4]) is False
