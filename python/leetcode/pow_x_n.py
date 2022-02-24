class Solution:
    def myPow(self, x: float, n: int) -> float:

        def traceback(x: float, n: int):
            if n == 1:
                return x

            if n == 0:
                return 1

            divided_power = n // 2
            res = traceback(x, divided_power)
            res *= res

            if n % 2 != 0:
                res = res * x

            return res

        res = traceback(x, abs(n))

        if n < 0:
            res = 1/res

        return round(res, 5)


if __name__ == "__main__":
    obj = Solution()

    assert obj.myPow(0.44894, n=-5) == 54.83508

    assert obj.myPow(0.44528, n=0) == 1

    assert obj.myPow(2.00000, n=-2) == 0.25000

    assert obj.myPow(2.10000, n=3) == 9.26100

    assert obj.myPow(2.00000, n=10) == 1024.00000
