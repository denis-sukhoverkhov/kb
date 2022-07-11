from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1

        for i in nums:
            if i == 0:
                return 0
            val = 1 if i > 0 else -1

            res *= val

        return res


if __name__ == "__main__":
    obj = Solution()

    nums = [-1, 1, -1, 1, -1]
    assert obj.arraySign(nums) == -1

    nums = [1, 5, 0, 2, -3]
    assert obj.arraySign(nums) == 0

    nums = [-1, -2, -3, -4, 3, 2, 1]
    assert obj.arraySign(nums) == 1
