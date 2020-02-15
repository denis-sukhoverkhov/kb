# BST Level-Order Traversal
# поиск вширину


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        if root is None:
            return
        values = []
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            temp_node = q.popleft()
            values.append(temp_node.data)
            if temp_node.left:
                q.append(temp_node.left)
            if temp_node.right:
                q.append(temp_node.right)
        print(*values, sep=' ')


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    myTree.levelOrder(root)
