class DoubleLinkedListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = DoubleLinkedListNode(None, None)
        self.right = DoubleLinkedListNode(None, None)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def insert(self, node: DoubleLinkedListNode):
        right = self.right
        left = right.prev

        left.next, right.prev = node, node
        node.next, node.prev = right, left

    def remove(self, node: DoubleLinkedListNode):
        left = node.prev
        right = node.next
        left.next, right.prev = right, left

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = DoubleLinkedListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)


# Your LRUCache object will be instantiated and called as such:
if __name__ == "__main__":
    obj = LRUCache(2)

    obj.put(1, 1)
    obj.put(2, 2)
    assert obj.get(1) == 1
    obj.put(3, 3)
    assert obj.get(2) == -1
