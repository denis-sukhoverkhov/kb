# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        current_node = root

        result = None
        while current_node:
            if current_node.val == val:
                result = current_node
                break
            elif current_node.val > val:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return result


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode(4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7))
    assert obj.searchBST(root, 2) is root.left
