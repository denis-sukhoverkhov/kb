class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        result = []
        for i in range(n):
            result.append([0] * n)

        all_elements = n * n
        filled_elements = 1

        i = j = start_j = start_i = 0
        max_i = max_j = n - 1
        while filled_elements <= all_elements:

            # -->
            for a in range(j, max_j + 1):
                result[i][a] = filled_elements
                filled_elements += 1
            j = max_j
            i += 1
            max_j -= 1

            # |
            # |
            # V
            for b in range(i, max_i + 1):
                result[b][j] = filled_elements
                filled_elements += 1
            i = max_i
            j -= 1
            max_i -=1

            # <--
            for a in range(j, start_j - 1, -1):
                result[i][a] = filled_elements
                filled_elements += 1
            j = start_j
            i -= 1

            for b in range(i, start_i, -1):
                result[b][j] = filled_elements
                filled_elements += 1

            start_i += 1
            start_j += 1

            i = j = start_i

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.generateMatrix(3) == [[1, 2, 3],
                                     [8, 9, 4],
                                     [7, 6, 5]]

    assert obj.generateMatrix(4) == [[ 1,  2,  3, 4],
                                     [12, 13, 14, 5],
                                     [11, 16, 15, 6],
                                     [10,  9,  8, 7],
                                     ]