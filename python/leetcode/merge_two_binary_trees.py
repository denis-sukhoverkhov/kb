from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[
        TreeNode]:

        if root1 is None and root2 is None:
            return None

        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0

        root1_left = root1.left if root1 else None
        root2_left = root2.left if root2 else None

        root1_right = root1.right if root1 else None
        root2_right = root2.right if root2 else None

        root = TreeNode(val=val1+val2,
                        left=self.mergeTrees(root1_left, root2_left),
                        right=self.mergeTrees(root1_right, root2_right))

        return root


if __name__ == "__main__":
    obj = Solution()

    root1 = [1, 3, 2, 5]
    root2 = [2, 1, 3, None, 4, None, 7]

    root1 = TreeNode.array_to_tree(root1)
    root2 = TreeNode.array_to_tree(root2)

    result = obj.mergeTrees(root1, root2).tree_to_arr()

    assert result == [3, 4, 5, 5, 4, None, 7]
