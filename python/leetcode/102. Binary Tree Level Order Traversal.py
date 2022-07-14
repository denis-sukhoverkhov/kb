# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from python.leetcode.libs.tree import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return []

        level = 0
        s = [(level, root)]
        while s:
            level, node = s.pop(0)

            if len(res) <= level:
                res.append([])

            res[level].append(node.val)

            level += 1
            if node.left:
                s.append((level, node.left))

            if node.right:
                s.append((level, node.right))

        return res


if __name__ == "__main__":
    obj = Solution()

    root = None
    assert obj.levelOrder(root) == []

    root = TreeNode.array_to_tree([1])
    assert obj.levelOrder(root) == [[1]]

    root = TreeNode.array_to_tree([3, 9, 20, None, None, 15, 7])
    assert obj.levelOrder(root) == [[3], [9, 20], [15, 7]]
