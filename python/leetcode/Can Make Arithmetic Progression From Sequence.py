from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        diff_prev = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff_prev:
                return False

        return True


if __name__ == "__main__":
    obj = Solution()

    arr = [3, 5, 1]
    assert obj.canMakeArithmeticProgression(arr) is True

    arr = [1, 2, 4]
    assert obj.canMakeArithmeticProgression(arr) is False