# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def traceback(left: TreeNode, right: TreeNode):

            if left is None and right is None:
                return True
            elif left is None or right is None or left.val != right.val:
                return False

            return traceback(left.left, right.right) and traceback(left.right, right.left)

        return traceback(left=root.left, right=root.right)


if __name__ == "__main__":
    obj = Solution()

    head = TreeNode(1, left=TreeNode(2, right=TreeNode(3)),
                    right=TreeNode(2, right=TreeNode(3)))
    assert obj.isSymmetric(head) is False

    head = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                    right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    assert obj.isSymmetric(head) is True

    head = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                    right=TreeNode(2, left=TreeNode(3), right=TreeNode(4)))
    assert obj.isSymmetric(head) is False

    head = TreeNode(1, left=TreeNode(2))
    assert obj.isSymmetric(head) is False

    head = TreeNode(1, )
    assert obj.isSymmetric(head) is True
