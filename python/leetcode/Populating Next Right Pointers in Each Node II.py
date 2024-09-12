from python.leetcode.libs.tree import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None

        def traceback(node):
            if node is None:
                return

            current_level_node = node
            dummy = Node()
            tmp_node = dummy
            while current_level_node:
                if current_level_node.left:
                    tmp_node.next = current_level_node.left
                    tmp_node = tmp_node.next

                if current_level_node.right:
                    tmp_node.next = current_level_node.right
                    tmp_node = tmp_node.next

                current_level_node = current_level_node.next

            traceback(dummy.next)

        traceback(root)

        return root


if __name__ == "__main__":
    obj = Solution()

    root = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
    root = Node.array_to_tree(root)
    result = obj.connect(root)

    root = [1, 2, 3, 4, 5, None, 7]
    root = Node.array_to_tree(root)

    obj.connect(root)

    assert obj.connect(None) is None
