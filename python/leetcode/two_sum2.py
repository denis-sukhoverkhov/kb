# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List, Optional


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> Optional[List[int]]:

        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            sum = numbers[p1] + numbers[p2]
            if sum == target:
                return [p1 + 1, p2 + 1]
            elif sum > target:
                p2 -= 1
            else:
                p1 += 1

        return None


if __name__ == "__main__":
    obj = Solution()

    assert obj.twoSum([-3, 3, 4, 90], 0) == [1, 2]

    assert obj.twoSum([-1, 0], -1) == [1, 2]

    assert obj.twoSum([-1, 0, 1], -1) == [1, 2]

    assert obj.twoSum([2, 7, 11, 15], 9) == [1, 2]

    assert obj.twoSum([2, 3, 4], 6) == [1, 3]
