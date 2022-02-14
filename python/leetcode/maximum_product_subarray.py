from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_product = nums[-1]

        prev = 1
        for i in range(len(nums)-1, -1, -1):
            product = prev * nums[i]
            prev = max(product, 1)
            max_product = max(max_product, product)

        return max_product


if __name__ == "__main__":
    obj = Solution()

    assert obj.maxProduct([-3, -1, -1]) == 6
    assert obj.maxProduct([2, 3, -2, 4]) == 6
