class Btree:

    def __init__(self, degree):
        self.degree = degree
        self.root = None

    def insert(self, k):

        if self.root is None:
            self.root = BtreeNode(self.degree, True)
            self.root.keys[0] = k
            self.root.n = 1
        else:
            if self.root.n == self.root.capacity:
                new_node = BtreeNode(self.degree, is_leaf=False)
                new_node.child_list[0] = self.root
                new_node.split_child(0, self.root)
                i = 0
                if new_node.keys[0] < k:
                    i += 1
                new_node.insert_non_full(k)
                self.root = new_node
            else:
                self.root.insert_non_full(k)


class BtreeNode:

    def __init__(self, degree: int, is_leaf: bool):
        self.degree = degree
        self.is_leaf = is_leaf
        self.keys = [None] * self.capacity
        self.child_list = [None] * self.capacity
        self.n = 0

    @property
    def capacity(self):
        return self.degree * 2 - 1

    def insert_non_full(self, k):

        idx = self.n - 1

        if self.is_leaf:
            while idx >= 0 and self.keys[idx] > k:
                self.keys[idx + 1] = self.keys[idx]
                idx -= 1

            self.keys[idx + 1] = k
            self.n += 1
        else:
            while idx >= 0 and self.keys[idx] > k:
                idx -= 1

            if self.child_list[idx + 1].n == self.capacity:
                self.split_child(idx+1, self.child_list[idx + 1])
                if self.keys[idx + 1] < k:
                    idx+=1

            self.child_list[idx + 1].insert_non_full(k)

    def split_child(self, i: int, root):
        z = BtreeNode(root.degree, root.is_leaf)
        z.n = root.degree - 1
        for j in range(0, self.degree - 1):
            z.keys[j] = root.keys[j + self.degree]
            root.keys[j + self.degree] = None

        if not root.is_leaf:
            for j in range(0, self.degree - 1):
                z.child_list[j] = root.child_list[j + self.degree]

        root.n = self.degree - 1

        for j in range(self.n, i + 2, -1):
            self.child_list[j + 1] = self.child_list[j]

        self.child_list[i + 1] = z

        for j in range(self.n - 1, i + 1, -1):
            self.keys[j + 1] = self.keys[j]

        self.keys[i] = root.keys[self.degree - 1]
        root.keys[self.degree - 1] = None

        self.n += 1


if __name__ == "__main__":
    btree = Btree(3)

    lst = [10, 20, 7, 40, 50, 25, 60, 70, 80]

    for i in lst:
        btree.insert(i)
