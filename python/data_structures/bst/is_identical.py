# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1

        if A is None and B is not None:
            return 0

        if B is None and A is not None:
            return 0

        if A.val == B.val and self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right):
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

    A = None
    for i in [1, 2, 3]:
        A = s.insert(A, i)

    B = None
    for i in [1, 2, 3]:
        B = s.insert(B, i)

    assert s.isSameTree(A, B) == 1

    for i in [7, 9]:
        B = s.insert(B, i)
    assert s.isSameTree(A, B) == 0

    for i in [7, 9]:
        A = s.insert(A, i)
    assert s.isSameTree(A, B) == 1
