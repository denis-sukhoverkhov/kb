from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        return goal == 0


if __name__ == "__main__":
    obj = Solution()

    assert obj.canJump([2, 5, 0, 0]) is True

    assert obj.canJump([2, 0]) is True

    assert obj.canJump([3, 2, 1, 0, 4]) is False

    assert obj.canJump([2, 3, 1, 1, 4]) is True
