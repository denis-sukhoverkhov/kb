from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        self.sums = [0]
        for i in range(0, len(nums)):
            self.sums.append(nums[i] + self.sums[i])

    def sumRange(self, left: int, right: int) -> int:
        right = right + 1
        res = self.sums[right] if left == 0 else self.sums[right] - self.sums[left]
        return res


if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])

    assert obj.sumRange(0, 2) == 1
    assert obj.sumRange(2, 5) == -1
    assert obj.sumRange(0, 5) == -3

