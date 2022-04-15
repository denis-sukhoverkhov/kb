import heapq
from typing import List


class Solution:
    # def maximumProduct(self, nums: List[int], k: int) -> int:
    #     while k > 0:
    #         heapq.heapify(nums)
    #
    #         nums[0] += 1
    #         k -= 1
    #
    #     result = 1
    #     mod = 10 ** 9 + 7
    #
    #     for i in nums:
    #         result = (result * i) % mod
    #
    #     return result

    def maximumProduct(self, nums: List[int], k: int) -> int:

        nums.sort()

        max_idx = len(nums) - 1
        curr_idx = 1
        prev_idx = 0
        while k > 0:

            if curr_idx > max_idx or nums[curr_idx] != nums[prev_idx]:
                nums[prev_idx] += 1
                k -= 1
                curr_idx = 1
                prev_idx = 0
            else:
                nums[prev_idx] += 1
                k -= 1
                prev_idx = curr_idx
                curr_idx += 1

        result = 1
        mod = 10 ** 9 + 7

        for i in nums:
            result = (result * i) % mod

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.maximumProduct([9, 7, 8], 9) == 1331

    assert obj.maximumProduct([1, 2, 3, 4, 5, 6, 7, 8], 10) == 1050000

    assert obj.maximumProduct([24, 5, 64, 53, 26, 38], 54) == 180820950

    nums = [6, 3, 3, 2]
    k = 2
    assert obj.maximumProduct(nums, k) == 216

    nums = [0, 4]
    k = 5
    assert obj.maximumProduct(nums, k) == 20
