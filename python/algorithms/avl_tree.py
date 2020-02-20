
class Node:
    def __init__(self, value: int, left = None, right = None, height: int = 1):
        self.value = value
        self.left = left
        self.right = right
        self.height = height


def get_height(root):

    return 0 if root is None else root.height


def get_balance(root: Node):
    if root is None:
        return 0

    return get_height(root.left) - get_height(root.right)


def left_rotate(z: Node):
    y = z.right
    t2 = y.left

    y.left = z
    z.right = t2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(z: Node):
    y = z.left
    t2 = y.right

    y.right = z
    z.left = t2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def insert(root: Node, key: int):
    if not root:
        return Node(key)
    elif key <= root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    
    balance = get_balance(root)
    if balance > 1 and key > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance > 1 and key < root.left.value:
        return right_rotate(root)

    if balance < -1 and key < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    if balance < -1 and key > root.right.value:
        return left_rotate(root)

    return root


if __name__ == "__main__":
    root = None

    lst = [10, 20, 30, 40, 50, 25]

    for i in lst:
        root = insert(root, i)
