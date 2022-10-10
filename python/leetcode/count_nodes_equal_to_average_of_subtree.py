from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        ct = 0

        def traverse(node,):
            nonlocal ct

            if node is None:
                return 0, 0

            result_left = traverse(node.left)

            result_right = traverse(node.right)
            new_ct = 1 + result_right[1] + result_left[1]
            new_summ = sum([node.val, result_left[0], result_right[0]])
            avg = int(new_summ / new_ct)

            if avg == node.val:
                ct += 1

            return new_summ, new_ct

        traverse(root)

        return ct


if __name__ == "__main__":
    obj = Solution()

    root = [1]
    root = TreeNode.array_to_tree(root)
    assert obj.averageOfSubtree(root) == 1

    root = [4, 8, 5, 0, 1, None, 6]
    root = TreeNode.array_to_tree(root)
    assert obj.averageOfSubtree(root) == 5
