from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = True

        def dfs(node):
            nonlocal res

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                res = False

            result = 1 + max(left, right)

            return result

        dfs(root)

        return res


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    assert obj.isBalanced(root) is False
