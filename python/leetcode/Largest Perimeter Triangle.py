from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)-1, -1, -1):
            if i-2 < 0:
                return 0

            a = nums[i]
            b = nums[i-1]
            c = nums[i-2]

            if a + b > c and a + c > b and b + c > a:
                return a + b + c

        return 0


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 1, 2]
    assert obj.largestPerimeter(nums) == 5

    nums = [1, 2, 1]
    assert obj.largestPerimeter(nums) == 0
