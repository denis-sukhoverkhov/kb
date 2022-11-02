from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = Counter(nums)
        # print(m)
        keys = list(m.keys())
        keys.sort()
        # print(keys)

        prev1, prev2 = 0, 0

        for i in range(len(keys)):
            val = keys[i]

            if i > 0 and val - 1 == keys[i - 1]:
                prev = prev1
            else:
                prev = prev2

            tmp = max(m[val] * val + prev, prev2)
            # print(prev1, prev2, tmp)

            prev1 = prev2
            prev2 = tmp

        return prev2


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 2, 3, 3, 3, 4]
    assert obj.deleteAndEarn(nums) == 9
