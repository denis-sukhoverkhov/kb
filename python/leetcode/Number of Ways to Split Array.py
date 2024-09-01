from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        ln = len(nums)

        res = 0
        sum_first_part = 0
        sum_second_part = sum(nums)
        for i in range(ln):
            sum_first_part += nums[i]
            sum_second_part -= nums[i]

            if sum_second_part > sum_first_part or i == ln - 1:
                continue

            res += 1

        return res


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 3, 1, 0]
    assert obj.waysToSplitArray(nums) == 2

    nums = [10, 4, -8, 7]
    assert obj.waysToSplitArray(nums) == 2
