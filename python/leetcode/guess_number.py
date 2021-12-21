# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def __init__(self, pick):
        self.pick = pick

    def guess(self, num):
        if num == self.pick:
            return 0
        elif num > self.pick:
            return -1
        else:
            return 1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            result = self.guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1


if __name__ == "__main__":

    pick = 6
    obj = Solution(pick)
    assert obj.guessNumber(10) == pick

    pick = 2
    obj = Solution(pick)
    assert obj.guessNumber(2) == pick

    pick = 1
    obj = Solution(pick)
    assert obj.guessNumber(2) == pick

    pick = 1
    obj = Solution(pick)
    assert obj.guessNumber(1) == pick

    pick = 99
    obj = Solution(pick)
    assert obj.guessNumber(100) == pick
