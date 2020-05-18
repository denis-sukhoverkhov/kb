# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if A is None:
            return A

        A.left, A.right = self.invertTree(A.right), self.invertTree(A.left)

        return A


if __name__ == "__main__":
    s = Solution()

    head = TreeNode(7)
    head.left = TreeNode(3)
    head.right = TreeNode(3)

    head.right.left = TreeNode(4)
    head.right.right = TreeNode(5)

    head.left.right = TreeNode(4)
    head.left.left = TreeNode(5)

    s.invertTree(head)
