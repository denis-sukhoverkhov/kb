# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if A is None:
            return 1
        lh = self.get_height(A.left)
        rh = self.get_height(A.right)

        if abs(lh - rh) <= 1 and self.isBalanced(A.left) is True and self.isBalanced(A.right) is True:
            return 1

        return 0

    def get_height(self, A):
        if A is None:
            return 0

        h = 1 + max(self.get_height(A.left), self.get_height(A.right))

        return h

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

    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)

    head.right.left = TreeNode(4)
    head.right.left.right = TreeNode(5)

    assert s.isBalanced(head) == 0


    head = None
    for i in [1, 2, 3]:
        head = s.insert(head, i)

    assert s.isBalanced(head) == 0
