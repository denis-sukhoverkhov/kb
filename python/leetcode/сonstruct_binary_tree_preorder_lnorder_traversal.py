# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrder(self, ) -> List[List[int]]:
        result = []

        def traceback(head: TreeNode, level: int):
            if head is None:
                return

            if len(result) > level:
                result[level].append(head.val)
            else:
                result.append([head.val])

            traceback(head.left, level+1)
            traceback(head.right, level+1)

        traceback(self, level=0)

        return result


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder and not inorder:
            return None

        root = TreeNode(val=preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder=preorder[1:mid+1], inorder=inorder[:mid])
        root.right = self.buildTree(preorder=preorder[mid+1:], inorder=inorder[mid+1:])

        return root


if __name__ == "__main__":
    obj = Solution()
    head = obj.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])

    result = head.levelOrder()
    assert result == [[3], [9, 20], [15, 7]]
