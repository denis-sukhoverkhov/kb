class Solution:
    def numberOfSteps(self, num: int) -> int:

        op = 0
        while num:
            if num & 1:
                op += 1
                num ^= 1
                continue

            num >>= 1
            op += 1

        return op


if __name__ == "__main__":
    obj = Solution()

    assert obj.numberOfSteps(14) == 6
