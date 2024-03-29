from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traceback(head: TreeNode, level: int):
            if head is None:
                return level

            return max(traceback(head.left, level+1), traceback(head.right, level+1))

        return traceback(root, 0)


if __name__ == "__main__":
    obj = Solution()

    head = TreeNode(3, left=TreeNode(9, left=TreeNode(11, right=TreeNode(14))),
                    right=TreeNode(20))
    assert obj.maxDepth(head) == 4

    head = TreeNode(3)
    assert obj.maxDepth(head) == 1

    head = TreeNode(3, left=TreeNode(9, left=TreeNode(11), right=TreeNode(14)),
                    right=TreeNode(20))
    assert obj.maxDepth(head) == 3
