# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def maxDepth(self, A):
        if A is None:
            return 0

        return 1 + max(self.maxDepth(A.left), self.maxDepth(A.right))

    def minDepth(self, A):
        if A is None:
            return 0

        if A.left is not None and A.right is not None:
            return 1 + min(self.minDepth(A.left), self.minDepth(A.right))

        return 1 + max(self.minDepth(A.left), self.minDepth(A.right))


if __name__ == "__main__":
    s = Solution()

    head = TreeNode(7)
    head.left = TreeNode(3)
    head.right = TreeNode(3)

    head.left.right = TreeNode(4)
    head.left.left = TreeNode(5)

    assert s.maxDepth(head) == 3

    assert s.minDepth(head) == 2

    s = Solution()
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.left.right = TreeNode(3)

    assert s.minDepth(head) == 3
