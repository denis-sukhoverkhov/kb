import collections


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def array_to_tree(cls, lst):
        root = cls(lst[0])
        q = collections.deque()
        q.append(root)

        idx = 1

        while q:
            node = q.popleft()

            if idx < len(lst):
                if lst[idx] is not None:
                    node.left = cls(lst[idx])
                    q.append(node.left)
                idx += 1

            if idx < len(lst):
                if lst[idx] is not None:
                    node.right = cls(lst[idx])
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


class Node(TreeNode):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.next = next
        super().__init__(val=val, left=left, right=right)