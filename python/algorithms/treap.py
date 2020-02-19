from random import random


class Node:
    def __init__(self, x, y, l = None, r = None):
        self.x = x
        self.y = y
        self.left = l
        self.right = r


def merge(n1: Node, n2: Node) -> Node:
    if n1 is None:
        return n2
    if n2 is None:
        return n1

    if n1.y < n2.y:
        n2.left = merge(n1, n2.left)
        return n2
    else:
        n1.right = merge(n1.right, n2)
        return n1


def split(x0: int, t: Node) -> (Node, Node):
    if t is None:
        return None, None

    if t.x <= x0:
        t1, t2 = split(x0, t.right)
        t.right = t1
        return t, t2
    else:
        t1, t2 = split(x0, t.left)
        t.left = t2
        return t1, t


def add(t1: Node, n: Node) -> Node:
    a, b = split(n.x, t1,)
    return merge(merge(a, n), b)


def delete(t: Node, x0: int) -> Node:
    a, b = split(x0, t)
    a1, _ = split(x0-1, a)
    return merge(a1, b)


if __name__ == "__main__":
    print("Дирамида aka Дуча aka Курево aka Декартово дерево")

    tree = None

    lst = [50, 17, 76, 9, 23, 54, 14, 19, 72, 12, 67]

    for i in lst:
        tree = add(tree, Node(x=i, y=random()))
