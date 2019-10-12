from queue import Queue


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrder(root):
    # Write your code here
    if root is None:
        return

    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


def postOrder(root):
    if root is None:
        return

    postOrder(root.left)
    postOrder(root.right)
    print(root.info, end=" ")


def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.info, end=" ")
    inOrder(root.right)


def height(root):
    if root.left is None and root.right is None:
        return 0
    else:
        l_height = 0
        if root.left:
            l_height = height(root.left)

        r_height = 0
        if root.right:
            r_height = height(root.right)

        return max(l_height, r_height) + 1


def levelOrder(root):
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.info, end=" ")
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)


def topView(root):
    temp_dct = {}

    def collect_node_info(node, height, hd, m):

        if node is None:
            return

        if hd not in m:
            m[hd] = (node.info, height)
        else:
            p = m[hd]

            if p[1] > height:
                m[hd] = (node.info, height)

        collect_node_info(node.left, height+1, hd-1, m)
        collect_node_info(node.right, height + 1, hd + 1, m)

    collect_node_info(root, 0, 0, temp_dct)

    for i in sorted(temp_dct.keys()):
        print(temp_dct[i][0], end=" ")


if __name__ == '__main__':

    tree = BinarySearchTree()

    for i in range(6):
        tree.create(i)

    # print(height(tree.root))

    topView(tree.root)
