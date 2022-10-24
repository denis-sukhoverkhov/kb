from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = (0, 0)
        right = (rows - 1, columns - 1)

        offset_elements = 0
        while left <= right:
            count_elements = (right[0] - left[0]) * columns + (right[1] - left[1] + 1)
            target_element = offset_elements + ((count_elements - 1) // 2)

            mid_coordinates = (target_element // columns, target_element % columns)

            mid_val = matrix[mid_coordinates[0]][mid_coordinates[1]]
            if mid_val == target:
                return True
            elif mid_val > target:
                right = self.get_prev_coordinates(columns, *mid_coordinates)
            else:
                offset_elements = target_element + 1
                left = self.get_next_coordinates(columns, *mid_coordinates)

        return False

    def get_prev_coordinates(self, columns, i, j):
        if j - 1 >= 0:
            return i, j - 1

        return i - 1, columns - 1

    def get_next_coordinates(self, columns, i, j):
        if j + 1 < columns:
            return i, j + 1

        return i + 1, 0


if __name__ == "__main__":
    obj = Solution()

    matrix = [[1, 5]]
    target = 5
    assert obj.searchMatrix(matrix, target) is True

    matrix = [[1, 1]]
    target = 2
    assert obj.searchMatrix(matrix, target) is False

    matrix = [[1]]
    target = 2
    assert obj.searchMatrix(matrix, target) is False

    matrix = [[1]]
    target = 1
    assert obj.searchMatrix(matrix, target) is True

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert obj.searchMatrix(matrix, target) is False

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert obj.searchMatrix(matrix, target) is True
