from typing import Optional
from python.leetcode.libs.tree import TreeNode



class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_identical(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and not node2 or node2 and not node1:
                return False

            if node1.val == node2.val \
                    and is_identical(node1.left, node2.left) \
                    and is_identical(node1.right, node2.right):
                return True

            return False

        res = False

        def search(node):
            nonlocal res

            if not node or res:
                return

            if node and node.val == subRoot.val:
                res = is_identical(node, subRoot)
                if res:
                    return

            search(node.left)
            search(node.right)

        search(root)

        return res


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([1, 1])
    subRoot = TreeNode.array_to_tree([1])
    assert obj.isSubtree(root, subRoot) is True

    root = TreeNode.array_to_tree([3, 4, 5, 1, None, 2])
    subRoot = TreeNode.array_to_tree([3, 1, 2])
    assert obj.isSubtree(root, subRoot) is False

    root = TreeNode.array_to_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = TreeNode.array_to_tree([4, 1, 2])
    assert obj.isSubtree(root, subRoot) is False

    root = TreeNode.array_to_tree([3, 4, 5, 1, 2])
    subRoot = TreeNode.array_to_tree([4, 1, 2])
    assert obj.isSubtree(root, subRoot)
