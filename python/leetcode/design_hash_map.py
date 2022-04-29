class MyHashMap:

    def __init__(self):
        self.hash_map_size = 1000
        self.buckets = [[] for _ in range(self.hash_map_size)]

    def get_idx(self, key):
        return key % self.hash_map_size

    def put(self, key: int, value: int) -> None:
        idx = self.get_idx(key)
        bucket = self.buckets[idx]

        for el in bucket:
            if el[0] == key:
                el[1] = value
                break
        else:
            bucket.append([key, value])

    def get(self, key: int) -> int:
        idx = self.get_idx(key)
        bucket = self.buckets[idx]

        for el in bucket:
            if el[0] == key:
                return el[1]

        return -1

    def remove(self, key: int) -> None:
        idx = self.get_idx(key)
        bucket = self.buckets[idx]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                break


if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)
    myHashMap.put(2, 2)
    assert myHashMap.get(1) == 1
    assert myHashMap.get(3) == -1
    myHashMap.put(2, 1)
    assert myHashMap.get(2) == 1
    myHashMap.remove(2)
    assert myHashMap.get(2) == -1
