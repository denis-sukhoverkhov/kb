# Definition for a binary tree node.
from typing import Optional
from python.leetcode.Convert_bst_to_greater_tree import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        current_node = root
        while current_node:
            self.stack.append(current_node)
            current_node = current_node.left

    def next(self) -> int:
        res = self.stack.pop()

        curr = res.right
        while curr:
            self.stack.append(curr)
            curr = curr.left

        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


if __name__ == "__main__":
    lst = [7, 3, 15, None, None, 9, 20]

    root = TreeNode.array_to_tree(lst)
    bSTIterator = BSTIterator(root)
    assert bSTIterator.next() == 3
    assert bSTIterator.next() == 7
    assert bSTIterator.hasNext() is True
    assert bSTIterator.next() == 9
    assert bSTIterator.hasNext() is True
    assert bSTIterator.next() == 15
    assert bSTIterator.hasNext() is True
    assert bSTIterator.next() == 20
    assert bSTIterator.hasNext() is False
