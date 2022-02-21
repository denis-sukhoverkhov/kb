from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        overflow = 1
        i = len(digits) - 1
        while overflow and i >= 0:
            result = digits[i] + overflow
            digits[i] = result % 10

            if result > 9:
                overflow = 1
            else:
                overflow = 0
                break

            i -= 1

        if overflow != 0:
            digits = [1] + digits

        return digits


if __name__ == "__main__":
    obj = Solution()

    assert obj.plusOne([9, 9]) == [1, 0, 0]
    assert obj.plusOne([1, 2, 3]) == [1, 2, 4]
    assert obj.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert obj.plusOne([9]) == [1, 0]
