from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        res = False

        def traceback(node, curr_summ):
            nonlocal res

            if not node:
                return

            if curr_summ + node.val == targetSum and node.right is None and node.left is None:
                res = True

            traceback(node.left, curr_summ+node.val)
            traceback(node.right, curr_summ+node.val)

        if not root:
            return False

        traceback(root, 0)

        return res


if __name__ == "__main__":
    obj = Solution()

    targetSum = 1
    root = TreeNode.array_to_tree([1, 2])
    assert obj.hasPathSum(root, targetSum) is False

    targetSum = 0
    assert obj.hasPathSum(None, targetSum) is False

    targetSum = 5
    root = TreeNode.array_to_tree([1, 2, 3])
    assert obj.hasPathSum(root, targetSum) is False

    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    root = TreeNode.array_to_tree(root)
    targetSum = 22
    assert obj.hasPathSum(root, targetSum) is True
