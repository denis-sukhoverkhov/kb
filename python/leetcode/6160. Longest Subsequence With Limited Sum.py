import bisect
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        res = []
        for q in queries:
            idx = bisect.bisect_left(nums, q)
            print(idx)


if __name__ == "__main__":
    obj = Solution()

    assert obj.answerQueries([4,5,2,1], [3,10,21]) == []