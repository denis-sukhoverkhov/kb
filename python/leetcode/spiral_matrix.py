class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m = len(matrix)
        n = len(matrix[0])
        result = []
        all_elements = m * n
        filled_elements = 1

        i = j = start_j = start_i = 0
        max_i = m - 1
        max_j = n - 1
        while filled_elements <= all_elements:

            # -->
            for a in range(j, max_j + 1):
                result.append(matrix[i][a])
                filled_elements += 1
            j = max_j
            i += 1
            max_j -= 1

            if filled_elements > all_elements:
                break

            # |
            # |
            # V
            for b in range(i, max_i + 1):
                result.append(matrix[b][j])
                filled_elements += 1
            i = max_i
            j -= 1
            max_i -= 1

            if filled_elements > all_elements:
                break

            # <--
            for a in range(j, start_j - 1, -1):
                result.append(matrix[i][a])
                filled_elements += 1
            j = start_j
            i -= 1

            if filled_elements > all_elements:
                break

            for b in range(i, start_i, -1):
                result.append(matrix[b][j])
                filled_elements += 1

            start_i += 1
            start_j += 1

            i = j = start_i

        return result


if __name__ == "__main__":
    obj = Solution()

    spiral_matrix = [
        [7],
        [9],
        [6],
    ]

    assert obj.spiralOrder(spiral_matrix) == [7, 9, 6]

    spiral_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    assert obj.spiralOrder(spiral_matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    spiral_matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

    assert obj.spiralOrder(spiral_matrix) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]

    spiral_matrix = [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ]
    assert obj.spiralOrder(spiral_matrix) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
