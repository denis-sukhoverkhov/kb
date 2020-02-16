from typing import Optional


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.ct_equal_elements = 1


def insert(head: Optional[Node], value):
    if head is None:
        return Node(value)
    elif head.value > value:
        head.left = insert(head.left, value)
    elif head.value < value:
        head.right = insert(head.right, value)
    else:
        head.ct_equal_elements += 1

    return head


def search(head: Optional[Node], value):
    if head is None:
        return None
    elif head.value == value:
        return head
    elif value < head.value:
        return search(head.left, value)
    elif value > head.value:
        return search(head.right, value)


def pre_order(head: Optional[Node]):
    """Прямой обход дерева"""
    if head is None:
        return None

    print(head.value, end=" ")
    pre_order(head.left)
    pre_order(head.right)


if __name__ == '__main__':
    root = None

    lst = [83, 75, 53, 10, 95, 83, 29, 48, 7, 35, 66, 45, 78, 24, 35, 44, 3, 99, 50, 92, 56, 42, 56, 84, 15, 89, 46, 56,
           96, 65, 63, 70, 8, 21, 62, 59, 26, 75, 54, 57, 70, 28, 87, 79, 37, 25, 23, 91, 67, 90, 27, 77, 93, 47, 29,
           15, 84, 66, 89, 56, 94, 20, 67, 81, 89, 55, 35, 59, 13, 70, 4]

    for i in lst:
        root = insert(root, i)

    node = search(root, 95)
    print(node.value)

    pre_order(root)
