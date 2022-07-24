import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        res = self.nums.copy()
        idx = len(res) - 1

        while idx > 0:
            i = random.randint(0, idx)
            res[i], res[idx] = res[idx], res[i]

            idx -= 1

        return res


if __name__ == "__main__":
    obj = Solution([1, 2, 3])

    obj.shuffle()
