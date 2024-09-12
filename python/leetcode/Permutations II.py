from collections import defaultdict
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        current = []
        len_nums = len(nums)

        m = defaultdict(int)
        for i in nums:
            m[i] += 1

        def traceback():
            if len(current) == len_nums:
                res.append(current.copy())
                return

            for k, v in m.items():
                if v > 0:
                    current.append(k)
                    m[k] -= 1
                    traceback()
                    current.pop()
                    m[k] += 1

        traceback()

        return res


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 1, 2]
    assert obj.permuteUnique(nums) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
