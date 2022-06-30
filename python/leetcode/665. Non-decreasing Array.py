from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        max_left = float('-inf')
        changed = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                changed += 1
                if nums[i] >= max_left:
                    nums[i - 1] = nums[i]
                    max_left = nums[i - 1]
                else:
                    nums[i] = nums[i - 1]
            max_left = max(max_left, nums[i-1])
            # print(max_left)
            # print(nums)
            if changed > 1:
                return False

        return True


if __name__ == "__main__":
    obj = Solution()
    assert obj.checkPossibility([4, 2, 3]) is True
    assert obj.checkPossibility([-1, 4, 2, 3]) is True
    assert obj.checkPossibility([5, 7, 1, 8]) is True
    assert obj.checkPossibility([3, 4, 2, 3]) is False
