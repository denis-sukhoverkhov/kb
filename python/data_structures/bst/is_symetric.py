# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):

        if A is None:
            return 1

        return self.isMirror(A.left, A.right)

    def isMirror(self, A, B):
        if not A and not B:
            return 1

        if A and not B:
            return 0

        if B and not A:
            return 0

        if A.val == B.val and self.isMirror(A.left, B.right) and self.isMirror(A.right, B.left):
            return 1

        return 0

    def insert(self, head, val):
        if head is None:
            return TreeNode(val)
        else:
            if val <= head.val:
                head.left = self.insert(head.left, val)
            else:
                head.right = self.insert(head.right, val)

        return head


if __name__ == "__main__":
    s = Solution()

    head = TreeNode(7)
    head.left = TreeNode(3)
    head.right = TreeNode(3)

    head.right.left = TreeNode(4)
    head.right.right = TreeNode(5)

    head.left.right = TreeNode(4)
    head.left.left = TreeNode(5)

    assert s.isSymmetric(head) == 1
