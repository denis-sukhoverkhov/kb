from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k == 0:
            return 0

        left, right = 0, 0
        product = 1
        ln = len(nums)
        result = 0

        while right < ln:
            product *= nums[right]

            while product >= k and left <= right:
                product /= nums[left]
                left += 1

            result += right - left + 1

            right += 1

        return result


if __name__ == "__main__":
    obj = Solution()
    assert obj.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert obj.numSubarrayProductLessThanK([1, 2, 3], 0) == 0
    assert obj.numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19) == 18
    assert obj.numSubarrayProductLessThanK([1, 1, 1], 1) == 0
