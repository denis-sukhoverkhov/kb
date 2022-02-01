from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = self.b_search(nums, target)
        right_idx = self.b_search(nums, target, left_bias=False)

        return [left_idx, right_idx]

    def b_search(self, nums, target, left_bias=True):
        lp, rp = 0, len(nums) - 1

        idx = -1
        while lp <= rp:
            mid = (lp + rp) // 2

            if nums[mid] > target:
                rp = mid - 1
            elif nums[mid] < target:
                lp = mid + 1
            else:
                idx = mid
                if left_bias:
                    rp = mid - 1
                else:
                    lp = mid + 1

        return idx


if __name__ == "__main__":
    obj = Solution()

    assert obj.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]

    assert obj.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert obj.searchRange([], 0) == [-1, -1]
