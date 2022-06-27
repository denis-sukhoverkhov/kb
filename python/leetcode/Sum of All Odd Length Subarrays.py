from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        sm = 0
        for ln in range(0, len(arr), 2):
            for j in range(0, len(arr) - ln):
                sm += sum(arr[j:j+ln+1])

        return sm


if __name__ == "__main__":
    obj = Solution()

    arr = [1, 4, 2, 5, 3]
    assert obj.sumOddLengthSubarrays(arr) == 58
