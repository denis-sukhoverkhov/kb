from typing import Optional, List
from python.leetcode.libs.tree import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def traceback(node):
            if node is None:
                return

            res.append(node.val)
            traceback(node.left)
            traceback(node.right)

        traceback(root)

        return res


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([1, None, 2, 3])
    assert obj.preorderTraversal(root) == [1, 2, 3]
