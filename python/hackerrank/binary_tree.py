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
    if root is None:
        return -1
    else:
        l_height = height(root.left)
        r_height = height(root.right)

        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1


tree = BinarySearchTree()
# t = int(input())

# arr = list(map(int, input().split()))

for i in range(10):
    tree.create(i)

preOrder(tree.root)
