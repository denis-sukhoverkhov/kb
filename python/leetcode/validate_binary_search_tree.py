from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def traceback(node, left, right):
            if node is None:
                return True

            if node.val <= left or node.val >= right:
                return False

            return traceback(node.left, left=left, right=node.val) \
                   and traceback(node.right, left=node.val, right=right)

        return traceback(root, float('-inf'), float('+inf'))


if __name__ == "__main__":
    obj = Solution()

    head = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    assert obj.isValidBST(head) is True

    head = TreeNode(5, left=TreeNode(4), right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
    assert obj.isValidBST(head) is False

    head = TreeNode(2, left=TreeNode(2), right=TreeNode(2))
    assert obj.isValidBST(head) is False

    head = TreeNode(5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6)))
    assert obj.isValidBST(head) is False

