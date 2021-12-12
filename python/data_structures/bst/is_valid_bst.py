# Definition for a  binary tree node
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        INT_MAX = 4294967296
        INT_MIN = -4294967296

        return int(self.util(A, mini=INT_MIN, maxi=INT_MAX))

    def util(self, node, mini, maxi):
        if node is None:
            return True

        if node.val < mini or node.val > maxi:
            return False

        return self.util(node.left, mini=mini, maxi=node.val - 1) and self.util(
            node.right, mini=node.val + 1, maxi=maxi
        )


if __name__ == "__main__":
    s = Solution()

    head = TreeNode(7)
    head.left = TreeNode(3)
    head.right = TreeNode(3)

    head.left.right = TreeNode(4)
    head.left.left = TreeNode(5)

    assert s.isValidBST(head) == 0
