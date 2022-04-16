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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _solution(node, summ=0):
            if node is None:
                return summ

            res_right = _solution(node.right, summ=summ)
            node.val += res_right
            res_left = _solution(node.left, summ=node.val)

            return res_left

        _solution(root)

        return root


if __name__ == "__main__":
    obj = Solution()

    lst = [0, -2, 3, None, -1, None, 4]
    root = TreeNode.array_to_tree(lst)
    res = obj.convertBST(root)
    assert root.tree_to_arr() == [7, 4, 7, None, 6, None, 4]

    lst = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    root = TreeNode.array_to_tree(lst)
    obj.convertBST(root)

    assert root.tree_to_arr() == [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None,
                                  None, 8]

