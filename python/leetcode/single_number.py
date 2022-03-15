from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.singleNumber([4, 1, 2, 1, 2]) == 4
