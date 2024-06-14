from python.leetcode.libs.tree import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        min_node, max_node = (p, q) if p.val < q.val else (q, p)

        answer = None

        def traceback(node):
            nonlocal answer
            if not node:
                return

            if node.val >= min_node.val and node.val <= max_node.val:
                answer = node
                return

            if node.val < min_node.val and node.val < max_node.val:
                traceback(node.right)
            else:
                traceback(node.left)

        traceback(root)

        return answer


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = 2
    q = 4
    assert obj.lowestCommonAncestor(root, root.left, root.left.right).val == root.left.val

    root = TreeNode.array_to_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert obj.lowestCommonAncestor(root, root.left, root.right).val == root.val
