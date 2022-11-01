from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        res = 0
        max_idx = 0

        def dfs(node, level):
            nonlocal res
            nonlocal max_idx

            if not node:
                return

            if level == max_idx:
                res += node.val
            elif level > max_idx:
                max_idx += 1
                res = node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return res


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
    assert obj.deepestLeavesSum(root) == 15

    root = TreeNode.array_to_tree([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
    assert obj.deepestLeavesSum(root) == 19
