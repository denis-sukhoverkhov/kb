class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low

        if diff % 2 != 0:
            diff += 1

        res = diff // 2

        if low % 2 != 0 and high % 2 != 0:
            res += 1

        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.countOdds(3, 7) == 3
    assert obj.countOdds(1, 11) == 6
    assert obj.countOdds(8, 10) == 1
