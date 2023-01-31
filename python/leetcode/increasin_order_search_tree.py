# Definition for a binary tree node.
import collections


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

    def __init__(self):
        self.tail = TreeNode()
        self.root = self.tail

    def increasingBST(self, root: TreeNode) -> TreeNode:

        def lrr_traverse(node):
            if node is None:
                return None

            lrr_traverse(node.left)
            self.tail.right = node
            node.left = None
            self.tail = self.tail.right
            lrr_traverse(node.right)

        lrr_traverse(root)

        return self.root.right


if __name__ == "__main__":
    obj = Solution()

    root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
    root = TreeNode.array_to_tree(root)
    tree = obj.increasingBST(root)

    assert tree.tree_to_arr() == [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8,
                                  None, 9]
