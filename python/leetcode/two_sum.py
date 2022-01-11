from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        _map = defaultdict(list)
        for i in range(len(nums)):
            _map[nums[i]].append(i)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in _map and diff != nums[i]:
                res = [_map[diff][0], i]
                res.sort()
                return res
            elif diff in _map and len(_map[diff]) > 1:
                return _map[diff]


if __name__ == "__main__":
    obj = Solution()

    assert obj.twoSum([3, 2, 4], 6) == [1, 2]

    assert obj.twoSum([3, 3], 6) == [0, 1]

    assert obj.twoSum([2, 7, 11, 15], 9) == [0, 1]
