from collections import defaultdict
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        m = defaultdict(int)

        new_array = []
        rows = len(nums)
        for i in range(rows):
            for j in range(len(nums[i])):
                m[nums[i][j]] += 1
                if m[nums[i][j]] == rows:
                    new_array.append(nums[i][j])

        new_array.sort()

        return new_array


if __name__ == "__main__":
    obj = Solution()

    nums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
    assert obj.intersection(nums) == [10,12,13,27,45]

    nums = [[1, 2, 3], [4, 5, 6]]
    assert obj.intersection(nums) == []

    nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
    assert obj.intersection(nums) == [3,4]