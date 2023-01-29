from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)

        rubber1 = 0
        rubber2 = 0
        for n in nums:
            tmp = max(rubber1 + n, rubber2)
            rubber1 = rubber2
            rubber2 = tmp

        return rubber2


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 3, 1, 1, 7]
    assert obj.rob(nums) == 11

    nums = [1, 2, 3, 1]
    assert obj.rob(nums) == 4

    nums = [2, 7, 9, 3, 1]
    assert obj.rob(nums) == 12
