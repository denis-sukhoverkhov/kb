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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        lp, rp = 0, len(nums)-1
        mid = (lp + rp) // 2

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


if __name__ == "__main__":
    obj = Solution()

    head = obj.sortedArrayToBST([-10, -3, 0, 5, 9])

    assert head.levelOrder() == [[0], [-10, 5], [-3, 9]]
