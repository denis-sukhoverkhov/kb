class Node:
    def __init__(self, val, key, next=None, prev=None):
        self.next = next  # reference to next node in DLL
        self.prev = prev  # reference to previous node in DLL
        self.val = val
        self.key = key


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.mp = {}
        self.first = None
        self.last = None

    # @return an integer
    def get(self, key):

        node = self.mp.get(key)
        if node:
            if len(self.mp) > 1 and node is not self.first:
                tmp_next = node.next
                tmp_prev = node.prev
                node.next = self.first
                self.first.prev = node
                node.prev = None
                self.first = node
                if tmp_prev is not None:
                    tmp_prev.next = tmp_next
                if tmp_next is not None:
                    tmp_next.prev = tmp_prev
                if node is self.last:
                    self.last = tmp_prev

            return node.val

        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # if key == '13':
        #     pass
        #     r = 3

        if key in self.mp:
            self.mp[key].val = value
            self.get(key)
            return

        if 0 < self.capacity == len(self.mp):
            del self.mp[self.last.key]
            self.last = self.last.prev
            if self.last is not None:
                self.last.next = None
            else:
                self.first = None

        old_first = self.first
        new_first = Node(next=self.first, key=key, val=value)
        self.first = new_first
        if old_first is not None:
            old_first.prev = self.first
        self.mp[key] = self.first

        if self.last is None:
            self.last = self.first


if __name__ == "__main__":

    # BIG TEST

    cmd = "95 11 S 1 1 G 11 G 11 S 3 10 G 10 S 3 12 S 1 15 S 4 12 G 15 S 8 6 S 5 3 G 2 G 12 G 10 S 11 5 G 7 S 5 1 S 15 5 G 2 S 13 8 G 3 S 14 2 S 12 11 S 7 10 S 5 4 G 9 G 2 S 13 5 S 10 14 S 9 11 G 5 S 13 11 S 8 12 G 10 S 5 12 G 8 G 11 G 8 S 9 11 S 10 6 S 7 12 S 1 7 G 10 G 9 G 15 G 15 G 3 S 15 4 G 10 G 14 G 10 G 12 G 12 S 14 7 G 11 S 9 10 S 6 12 S 14 11 G 3 S 7 5 S 1 14 S 2 8 S 11 12 S 8 4 G 3 S 13 15 S 1 4 S 5 3 G 3 G 9 G 14 G 9 S 13 10 G 14 S 3 9 G 8 S 3 5 S 6 4 S 10 3 S 11 13 G 8 G 4 S 2 11 G 2 G 9 S 15 1 G 9 S 7 8 S 4 3 G 3 G 1 S 8 4 G 13 S 1 2 G 3"
    lst = cmd.split(" ")
    iter_ct = int(lst[0])
    capacity = int(lst[1])
    cache = LRUCache(capacity)

    ct = 0
    operations = lst[2:]
    op_counter = 0
    while op_counter < iter_ct:
        op = operations[ct]
        if op == "S":
            cache.set(operations[ct + 1], operations[ct + 2])
            ct += 3
        else:
            print(cache.get(operations[ct + 1], ))
            ct += 2
        op_counter += 1

    # ==========
    capacity = 1
    cache = LRUCache(capacity)

    cache.set(2, 1)
    cache.set(2, 2)
    assert cache.get(2) == 2
    cache.set(1, 1)
    cache.set(4, 1)
    assert cache.get(2) == -1

    capacity = 0
    cache = LRUCache(capacity)

    assert cache.get(5) == -1

    cache.set(1, 10)
    cache.set(2, 20)
    cache.set(3, 30)
    cache.set(4, 40)
    assert cache.get(1) == 10
    assert cache.get(2) == 20
    assert cache.get(3) == 30
    assert cache.get(4) == 40

    capacity = 2
    cache = LRUCache(capacity)

    assert cache.get(5) == -1

    cache.set(1, 10)
    assert cache.get(1) == 10

    cache.set(5, 12)
    assert cache.get(5) == 12

    assert cache.get(1) == 10
    assert cache.get(5) == 12
    assert cache.get(10) == -1

    assert cache.get(1) == 10
    assert cache.get(1) == 10
    cache.set(6, 14)
    assert cache.get(5) == -1
    assert cache.get(6) == 14
    assert cache.get(1) == 10
