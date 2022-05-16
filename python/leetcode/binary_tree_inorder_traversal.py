from typing import Optional, List
from python.leetcode.libs.tree import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traceback(root: TreeNode):
            if root is None:
                return

            traceback(root.left)
            result.append(root.val)
            traceback(root.right)

        traceback(root)

        return result


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
    assert obj.inorderTraversal(root) == [1, 3, 2]

    root = TreeNode(1)
    assert obj.inorderTraversal(root) == [1]
