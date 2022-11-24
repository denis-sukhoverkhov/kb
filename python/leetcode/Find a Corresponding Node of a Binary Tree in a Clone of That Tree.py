import copy

from python.leetcode.libs.tree import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        result = None

        def dfs(orig_node, clone_node):
            nonlocal result

            if not orig_node:
                return

            if orig_node is target:
                result = clone_node
                return

            dfs(orig_node.left, clone_node.left)
            dfs(orig_node.right, clone_node.right)

        dfs(original, cloned)

        return result


if __name__ == "__main__":
    obj = Solution()

    orig = TreeNode.array_to_tree([8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1])
    clone = copy.deepcopy(orig)
    assert obj.getTargetCopy(orig, clone, orig.right.right.right) is clone.right.right.right

    orig = TreeNode.array_to_tree([7])
    clone = copy.deepcopy(orig)
    assert obj.getTargetCopy(orig, clone, orig) is clone

    orig = TreeNode.array_to_tree([7, 4, 3, None, None, 6, 19])
    clone = copy.deepcopy(orig)
    assert obj.getTargetCopy(orig, clone, orig.right) is clone.right
