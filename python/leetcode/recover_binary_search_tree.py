# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def array_to_tree(cls, lst):
        root = TreeNode(lst[0])
        q = collections.deque()
        q.append(root)

        idx = 1

        while q:
            node = q.popleft()

            if idx < len(lst):
                if lst[idx] is not None:
                    node.left = TreeNode(lst[idx])
                    q.append(node.left)
                idx += 1

            if idx < len(lst):
                if lst[idx] is not None:
                    node.right = TreeNode(lst[idx])
                    q.append(node.right)
                idx += 1

        return root

    def tree_to_arr(self):
        res = []

        q = collections.deque()
        q.append(self)

        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)

        while not res[-1]:
            res.pop()

        return res


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        nodes = []

        def _inorder_traversal(node):
            if node is None:
                return

            _inorder_traversal(node.left)

            nodes.append(node)

            _inorder_traversal(node.right)

        _inorder_traversal(root)

        sorted_values = sorted([n.val for n in nodes])

        for i in range(len(sorted_values)):
            nodes[i].val = sorted_values[i]


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([3, 1, 4, None, None, 2])
    obj.recoverTree(root)
    assert root.tree_to_arr() == [2, 1, 4, None, None, 3]

    root = TreeNode.array_to_tree([1, 3, None, None, 2])
    obj.recoverTree(root)
    assert root.tree_to_arr() == [3, 1, None, None, 2]
