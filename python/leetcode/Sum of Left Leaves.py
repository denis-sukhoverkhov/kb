from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        res = 0

        def traceback(left, right):
            nonlocal res

            if left and left.right is None and left.left is None:
                res += left.val

            if left:
                traceback(left.left, left.right)

            if right:
                traceback(right.left, right.right)

        traceback(root.left, root.right)

        return res


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([3, 9, 20, None, None, 15, 7])
    assert obj.sumOfLeftLeaves(root) == 24

    root = TreeNode.array_to_tree([1])
    assert obj.sumOfLeftLeaves(root) == 0

