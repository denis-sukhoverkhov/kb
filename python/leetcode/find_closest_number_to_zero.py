from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distance = nums[0]

        for i in nums:
            if abs(i) < abs(distance) or (abs(i) == abs(distance) and distance < i):

                distance = i

        return distance


if __name__ == "__main__":
    obj = Solution()

    nums = [2, -1, 1]
    assert obj.findClosestNumber(nums) == 1

    nums = [-4, -2, 1, 4, 8]
    assert obj.findClosestNumber(nums) == 1
