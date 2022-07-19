# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from python.leetcode.libs.tree import TreeNode


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        def traverse(node, level):
            if not node:
                return 0

            if node.val == B:
                return level

            left_res = traverse(node.left, level + 1)
            if left_res == 1:
                return node.right

            right_res = traverse(node.right, level + 1)
            if right_res == 1:
                return node.left

            res = max(right_res, left_res)

            if res:
                return res - 1

            return 0

        res = traverse(A, 0)

        if not res:
            return []

        ans = []

        if isinstance(res, TreeNode):
            if res.left:
                ans.append(res.left.val)

            if res.right:
                ans.append(res.right.val)

        return ans


if __name__ == "__main__":
    obj = Solution()

    A = TreeNode.array_to_tree([1, 2, None, None, 3, 4, 5])
    assert obj.solve(A, 4) == []

    A = TreeNode.array_to_tree([1, 2, 3, 4, 5, 6, 7])
    assert obj.solve(A, 4) == [6, 7]

    A = TreeNode.array_to_tree([1, 2, 3, 4, 5, 6 ])
    assert obj.solve(A, 1) == []

    A = TreeNode.array_to_tree([1, 2, 3, 4, 5, 6, 7])
    assert obj.solve(A, 5) == [6, 7]
