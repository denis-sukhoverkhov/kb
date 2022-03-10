from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            mid = (lp + rp) // 2

            if nums[mid] == target:
                return mid

            if nums[lp] <= nums[mid]:
                if target > nums[mid] or target < nums[lp]:
                    lp = mid + 1
                else:
                    rp = mid - 1
            else:
                if target < nums[mid] or target > nums[rp]:
                    rp = mid - 1
                else:
                    lp = mid + 1

        return -1


if __name__ == "__main__":
    obj = Solution()

    assert obj.search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4

    assert obj.search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    assert obj.search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    assert obj.search([1], 0) == -1
