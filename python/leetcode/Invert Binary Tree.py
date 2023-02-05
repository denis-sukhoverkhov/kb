from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node: TreeNode):
            if not node:
                return

            node.left, node.right = node.right, node.left

            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return root


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([4, 2, 7, 1, 3, 6, 9])
    obj.invertTree(root)
