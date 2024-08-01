from typing import List

from python.leetcode.libs.tree import ArrayNode as Node


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        res = []

        def traversal(node, level):
            if node is None:
                return

            if len(res) > level:
                res[level].append(node.val)
            else:
                res.append([node.val])

            for child in node.children:
                traversal(child, level + 1)

        traversal(root, 0)

        return res


if __name__ == "__main__":
    obj = Solution()

    root = Node.array_to_tree([1, None, 3, 2, 4, None, 5, 6])
    assert obj.levelOrder(root) == [[1], [3, 2, 4], [5, 6]]
