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


def min_value_node(head: Optional[Node]):
    cur = head

    while cur.left is not None:
        cur = cur.left
    return cur


def delete(head: Optional[Node], value):

    if head is None:
        return head

    if value < head.value:
        head.left = delete(head.left, value)
    elif value > head.value:
        head.right = delete(head.right, value)
    else:
        if head.ct_equal_elements > 1:
            head.ct_equal_elements -= 1
            return head

        if head.left is None:
            temp = head.right
            return temp
        elif head.right is None:
            temp = head.left
            return temp

        temp = min_value_node(head.right)
        head.value = temp.value
        head.right = delete(head.right, temp.value)

    return head


def pre_order(head: Optional[Node]):
    """Прямой обход дерева"""
    if head is None:
        return None

    print(head.value, end=" ")
    pre_order(head.left)
    pre_order(head.right)


def in_order(head: Optional[Node]):
    """Центрированный обход дерева(сортровка по возрастанию)"""
    if head is None:
        return None

    in_order(head.left)
    print(head.value, end=" ")  # sort
    in_order(head.right)


def in_order2(head: Optional[Node]):
    """Центрированный обход дерева(сортировка по убыванию)"""
    if head is None:
        return None

    in_order2(head.right)
    print(head.value, end=" ")  # sort
    in_order2(head.left)


def post_order(head: Optional[Node]):
    """Обратный обход дерева(от листьев к корневым элементам)"""
    if head is None:
        return

    post_order(head.right)
    post_order(head.left)
    print(head.value, end=" ")


if __name__ == '__main__':
    root = None

    lst = [50, 17, 76, 9, 23, 54, 14, 19, 72, 12, 67, 54]

    for i in lst:
        root = insert(root, i)

    node = search(root, 95)
    print(node)

    print("pre_order: ", end="")
    pre_order(root)

    print("\nin_order: ", end="")
    in_order(root)

    print("\nin_order2: ", end="")
    in_order2(root)

    print("\npost_order: ", end="")
    post_order(root)

    root = delete(root, 54)

    print("\nin_order: ", end="")
    in_order(root)
