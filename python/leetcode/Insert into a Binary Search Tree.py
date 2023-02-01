from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def bst(node):
            if not node:
                return

            if node.val < val and node.right is None:
                node.right = TreeNode(val)
                return

            if node.val > val and node.left is None:
                node.left = TreeNode(val)
                return

            if node.val < val:
                bst(node.right)
            else:
                bst(node.left)

        if not root:
            return TreeNode(val)

        bst(root)

        return root


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([8, None, 55, 39, None, 11, None, None, 23, None, None])
    val = 17
    assert obj.insertIntoBST(root, val).val == root.val

    root = TreeNode.array_to_tree([8, None, 55, 39, None, 11, None, None, 23, None, None])
    val = 17
    assert obj.insertIntoBST(root, val).val == root.val

    root = TreeNode.array_to_tree([4, 2, 7, 1, 3])
    val = 5
    assert obj.insertIntoBST(root, val).val == root.val
