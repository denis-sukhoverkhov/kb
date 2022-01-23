# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def traceback(head: TreeNode, level: int):
            if head is None:
                return

            if len(result) > level:
                result[level].append(head.val)
            else:
                result.append([head.val])

            traceback(head.left, level + 1)
            traceback(head.right, level + 1)

        traceback(root, level=0,)

        for i in range(len(result)):
            if i % 2 != 0:
                result[i] = result[i][::-1]
        return result


if __name__ == "__main__":
    obj = Solution()

    head = TreeNode(3, left=TreeNode(9, left=TreeNode(11), right=TreeNode(14)), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    assert obj.zigzagLevelOrder(head) == [[3], [20, 9], [11, 14, 15, 7]]

    head = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    assert obj.zigzagLevelOrder(head) == [[3], [20, 9], [15, 7]]

    head = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, right=TreeNode(5)))
    assert obj.zigzagLevelOrder(head) == [[1], [3, 2], [4, 5]]

