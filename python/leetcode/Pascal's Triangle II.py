from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [1] * (rowIndex + 1)

        if rowIndex <= 1:
            return row[:rowIndex + 1]

        for i in range(1, rowIndex):
            prev = row[0]
            for j in range(1, i + 1):
                tmp = row[j]
                row[j] += prev
                prev = tmp

        return row


if __name__ == "__main__":
    obj = Solution()

    assert obj.getRow(5) == [1, 5, 10, 10, 5, 1]
    assert obj.getRow(3) == [1, 3, 3, 1]
    assert obj.getRow(4) == [1, 4, 6, 4, 1]
    assert obj.getRow(0) == [1]
    assert obj.getRow(1) == [1, 1]
