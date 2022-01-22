# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def traceback(head: TreeNode, level: int):
            if head is None:
                return

            if len(result) > level:
                result[level].append(head.val)
            else:
                result.append([head.val])

            traceback(head.left, level+1)
            traceback(head.right, level+1)

        traceback(root, level=0)

        return result


if __name__ == "__main__":
    obj = Solution()

    head = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))

    assert obj.levelOrder(head) == [[3], [9, 20], [15, 7]]
