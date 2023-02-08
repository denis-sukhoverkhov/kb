# Definition for a binary tree node.
import collections
from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0
        result = 0

        def lrr_traverse(node):
            nonlocal counter, result

            if node is None:
                return

            lrr_traverse(node.left)

            counter += 1

            if counter == k:
                result = node.val
                return

            lrr_traverse(node.right)

        lrr_traverse(root)

        return result


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([5, 3, 6, 2, 4, None, None, 1])
    assert obj.kthSmallest(root=root, k=3) == 3

    root = TreeNode.array_to_tree([3, 1, 4, None, 2])
    assert obj.kthSmallest(root=root, k=1) == 1
