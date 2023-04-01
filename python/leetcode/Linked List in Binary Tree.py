from typing import Optional

from python.leetcode.libs.linked_list import ListNode
from python.leetcode.libs.tree import TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def is_identical(tree_node, list_node):
            if list_node is None:
                return True

            if tree_node is None or tree_node.val != list_node.val:
                return False

            left = is_identical(tree_node.left, list_node.next)
            right = is_identical(tree_node.right, list_node.next)

            return left or right

        res = False

        def search(node):
            nonlocal res

            if node is None:
                return

            if node.val == head.val and is_identical(tree_node=node, list_node=head):
                res = True
                return

            search(node.left)
            search(node.right)

        search(root)

        return res


if __name__ == "__main__":
    obj = Solution()

    head = ListNode.to_list([1, 4, 2, 6, 8])
    root = TreeNode.array_to_tree(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    assert obj.isSubPath(head, root) is False

    head = ListNode.to_list([4, 2, 8])
    root = TreeNode.array_to_tree(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    assert obj.isSubPath(head, root)

    head = ListNode.to_list([1, 4, 2, 6])
    root = TreeNode.array_to_tree(
        [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3])
    assert obj.isSubPath(head, root)
