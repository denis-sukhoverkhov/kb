class MyHashSet:

    def __init__(self):
        self.numBuckets = 1
        self.buckets = [[] for _ in range(self.numBuckets)]

    def get_idx(self, key):
        idx = key % self.numBuckets
        return idx

    def add(self, key: int) -> None:
        idx = self.get_idx(key)
        if not self.contains(key):
            self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self.get_idx(key)
        if self.contains(key):
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self.get_idx(key)
        return key in self.buckets[idx]


if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)
    myHashSet.add(2)
    assert myHashSet.contains(1) is True
    assert myHashSet.contains(3) is False
    myHashSet.add(2)
    assert myHashSet.contains(2) is True
    myHashSet.remove(2)
    assert myHashSet.contains(2) is False
