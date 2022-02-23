
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if root is None:
            return None

        def traceback(left, right):

            if left is None or right is None:
                return None

            left.next = right

            traceback(left.left, left.right)
            traceback(left.right, right.left)
            traceback(right.left, right.right)

        traceback(root.left, root.right)

        return root


if __name__ == "__main__":
    obj = Solution()

    root = Node(1, left=Node(2, left=Node(4), right=Node(5)),
                right=Node(3, left=Node(6), right=Node(7)))
    assert obj.connect(root)
