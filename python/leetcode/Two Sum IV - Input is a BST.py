from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        m = set()

        is_exist_target = False

        def traverse(node: TreeNode):
            nonlocal is_exist_target

            if node is None or is_exist_target:
                return

            diff = k - node.val

            if diff in m:
                is_exist_target = True

            m.add(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        return is_exist_target


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([5, 3, 6, 2, 4, None, 7])
    k = 9
    assert obj.findTarget(root, k) is True

