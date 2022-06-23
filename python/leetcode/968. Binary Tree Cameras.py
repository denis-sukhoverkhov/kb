from typing import Optional

from python.leetcode.libs.tree import TreeNode


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        covered_nodes = set()

        allocated_cameras = set()

        def dfs(node, parent):
            if node is None:
                return

            dfs(node.left, node)

            if node.left and node.left not in covered_nodes:
                allocated_cameras.add(node)
                covered_nodes.add(node)
                covered_nodes.add(node.left)
                covered_nodes.add(parent)
                if node.right:
                    covered_nodes.add(node.right)

            dfs(node.right, node)

            if node.right and node.right not in covered_nodes:
                allocated_cameras.add(node)
                covered_nodes.add(node)
                covered_nodes.add(node.right)
                covered_nodes.add(parent)

        dfs(root, None)

        if root not in allocated_cameras and root not in covered_nodes:
            allocated_cameras.add(root)

        res = len(allocated_cameras)
        if res == 0 and root:
            res = 1

        # print([i.val for i in allocated_cameras])
        return res


if __name__ == "__main__":
    obj = Solution()

    root = TreeNode.array_to_tree(
        [0, None, 1, None, 2, None, 3])
    assert obj.minCameraCover(root) == 2

    root = TreeNode.array_to_tree(
        [0, 1, 2, 3, None, None, 4, 5, 6, 7, None, None, 8, 9, 10, 11, 12, None, None, 13, 14, None,
         None, None, None, 15, 16])
    assert obj.minCameraCover(root) == 6

    root = TreeNode.array_to_tree([0, 1, 2])
    assert obj.minCameraCover(root) == 1

    root = TreeNode.array_to_tree([0])
    assert obj.minCameraCover(root) == 1

    root = TreeNode.array_to_tree([0,
                                   1, 2,
                                   3, None, None, 4,
                                   5, 6, 7, None,
                                   None, 8, 9, 10, 11, 12,
                                   None, None, 13, 14, None, None, None, None, 15, 16])
    assert obj.minCameraCover(root) == 6

    root = TreeNode.array_to_tree([0, 0, None, 0, None, 0, None, None, 0])
    assert obj.minCameraCover(root) == 2

    root = TreeNode.array_to_tree([0, 0, None, 0, None, 0, None, None, 0])
    assert obj.minCameraCover(root) == 2

    root = TreeNode.array_to_tree([0, 0, None, 0, 0])
    assert obj.minCameraCover(root) == 1

# [0,1,2,3, None,None, 4,5, 6, 7,None,None, 8,9, 10, 11, 12, None, None, 13, 14, None, None, None, None, 15, 16]
