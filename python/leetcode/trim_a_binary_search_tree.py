# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.arr = []

    def to_array(self, tree_node):
        if not tree_node:
            self.arr.append(None)
            return

        self.arr.append(tree_node.val)

        self.to_array(tree_node.left)
        self.to_array(tree_node.right)


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def _trim(node):
            if node is None:
                return

            if low <= node.val <= high:
                node.right = _trim(node.right)
                node.left = _trim((node.left))
                return node

            if node.val > high:
                return _trim(node.left)

            if node.val < low:
                return _trim(node.right)

        return _trim(root)


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode(3, left=TreeNode(0, right=TreeNode(2, left=TreeNode(1))), right=TreeNode(4))

    result = obj.trimBST(root, 1, 3)
    result.to_array(result)
    assert result.arr == [3, 2, None, 1, None, None, None]

    root = TreeNode(1, left=TreeNode(0), right=TreeNode(2))

    result = obj.trimBST(root, 1, 2)
    result.to_array(result)
    assert result.arr == [1, None, 2, None, None]
