from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1, p2 = 0, 0

        curr_sum = 0
        min_len = float('inf')
        while p1 < len(nums):

            if curr_sum < target and p2 >= len(nums):
                break

            if curr_sum < target and p2 < len(nums):
                curr_sum += nums[p2]
                p2 += 1
                continue

            min_len = min(p2 - p1, min_len)

            curr_sum -= nums[p1]
            p1 += 1

        return min_len if min_len != float('inf') else 0


if __name__ == "__main__":
    obj = Solution()

    target = 15
    nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
    assert obj.minSubArrayLen(target, nums) == 2

    target = 11
    nums = [1, 2, 3, 4, 5]
    assert obj.minSubArrayLen(target, nums) == 3

    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    assert obj.minSubArrayLen(target, nums) == 0

    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    assert obj.minSubArrayLen(target, nums) == 2
