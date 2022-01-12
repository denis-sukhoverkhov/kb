from math import gcd
from typing import List


class Solution(object):

    def rotate(self, nums: List[int], k: int) -> None:
        moveto = 0
        i = 0
        for _ in range(len(nums)):
            moveto = (moveto + k) % len(nums)
            if moveto == i:
                i += 1
                moveto = i
            else:
                nums[moveto], nums[i] = nums[i], nums[moveto]


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    obj.rotate(nums, 2)
    assert nums == [2, 1]

    nums = [1, 2]
    obj.rotate(nums, 5)
    assert nums == [2, 1]

    nums = [1, 2, 3]
    obj.rotate(nums, 4)
    assert nums == [3, 1, 2]

    nums = [1, 2]
    obj.rotate(nums, 2)
    assert nums == [1, 2]

    nums = [1, 2]
    obj.rotate(nums, 3)
    assert nums == [2, 1]

    nums = [1, 2, 3, 4, 5, 6, 7]
    obj.rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    obj.rotate(nums, 2)
    assert nums == [3, 99, -1, -100]
