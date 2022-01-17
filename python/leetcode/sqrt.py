class Solution:
    def mySqrt(self, x: int) -> int:
        lp, rp = 0, x

        while lp <= rp:
            mid = (lp + rp) // 2

            if mid*mid == x:
                return mid

            if mid*mid > x:
                rp = mid - 1
            else:
                lp = mid + 1

        if rp * rp <= x:
            return rp

        return lp


if __name__ == "__main__":
    obj = Solution()

    assert obj.mySqrt(8) == 2
    assert obj.mySqrt(4) == 2

