class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        summ = 0
        power = 1
        while n:
            digit = n % 10
            n = n // 10
            summ += digit
            power *= digit

        return power - summ


if __name__ == "__main__":
    obj = Solution()

    n = 234
    assert obj.subtractProductAndSum(n) == 15
