from typing import Optional, List

from python.leetcode.libs.linked_list import ListNode


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        max_row = m - 1
        max_column = n - 1

        current_node = head

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def traceback(i, j, d):
            nonlocal current_node
            if i > max_row or j > max_column or current_node is None or matrix[i][j] != -1:
                return

            matrix[i][j] = current_node.val
            current_node = current_node.next

            for _ in range(len(directions)):
                x, y = directions[d]
                traceback(i + x, j + y, d)
                d = (d + 1) % len(directions)

        traceback(0, 0, 0)

        return matrix


if __name__ == "__main__":
    obj = Solution()

    m = 4
    n = 5
    head = ListNode.to_list(
        [515, 942, 528, 483, 20, 159, 868, 999, 474, 320, 734, 956, 12, 124, 224, 252, 909, 732])
    assert obj.spiralMatrix(m, n, head) == [[515, 942, 528, 483,  20],
                                            [124, 224, 252, 909, 159],
                                            [12,   -1,  -1, 732, 868],
                                            [956, 734, 320, 474, 999]]

    m = 3
    n = 5
    head = ListNode.to_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
    assert obj.spiralMatrix(m, n, head) == [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]

    m = 1
    n = 4
    head = ListNode.to_list([0, 1, 2])
    assert obj.spiralMatrix(m, n, head) == [[0, 1, 2, -1]]
