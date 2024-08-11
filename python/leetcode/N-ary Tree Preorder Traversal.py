from typing import List

from python.leetcode.libs.tree import ArrayNode as Node


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        res = []

        def preorder_traversal(node):
            if not node:
                return

            res.append(node.val)

            for i in node.children:
                preorder_traversal(i)

        preorder_traversal(root)

        return res


if __name__ == "__main__":
    obj = Solution()

    root = [1, None, 3, 2, 4, None, 5, 6]
    root = Node.array_to_tree(root)
    assert obj.preorder(root) == [1, 3, 5, 6, 2, 4]
