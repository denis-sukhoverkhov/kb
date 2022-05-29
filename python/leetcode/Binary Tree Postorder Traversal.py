from typing import Optional, List

from python.leetcode.libs.tree import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def traceback(node):
            if node is None:
                return

            traceback(node.left)
            traceback(node.right)
            result.append(node.val)

        traceback(root)

        return result


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([1, None, 2, 3])
    assert obj.postorderTraversal(root) == [3, 2, 1]

    root = TreeNode.array_to_tree([3, 1, 2])
    assert obj.postorderTraversal(root) == [1, 2, 3]