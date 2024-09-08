from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()

        mi_v = nums[0]
        res = 1
        for i in range(len(nums)):
            if nums[i] - mi_v > k:
                res += 1
                mi_v = nums[i]
        return res


if __name__ == "__main__":
    obj = Solution()

    nums = [16, 8, 17, 0, 3, 17, 8, 20]
    k = 10
    assert obj.partitionArray(nums, k) == 2

    nums = [3, 6, 1, 2, 5]
    k = 2
    assert obj.partitionArray(nums, k) == 2

    nums = [1, 2, 3]
    k = 1
    assert obj.partitionArray(nums, k) == 2
