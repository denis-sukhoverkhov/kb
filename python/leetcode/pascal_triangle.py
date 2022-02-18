from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [
            [1],
            [1, 1]
        ]

        if numRows < 3:
            return result[:numRows]

        for i in range(2, numRows):
            new_row = [1] * (i + 1)

            for j in range(1, len(new_row) - 1):
                new_row[j] = result[-1][j-1] + result[-1][j]

            result.append(new_row)

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    assert obj.generate(3) == [[1], [1, 1], [1, 2, 1]]
    assert obj.generate(0) == []
    assert obj.generate(1) == [[1]]
    assert obj.generate(2) == [[1], [1, 1]]

