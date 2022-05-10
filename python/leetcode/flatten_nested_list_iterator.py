from python.leetcode.libs.nested_integer import NestedInteger


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.lst = []
        self.pointer = 0

        def traversal(lst):
            if lst.isInteger():
                self.lst.append(lst)
                return

            for k in lst.getList():
                traversal(k)

        for i in nestedList:
            traversal(i)

    def next(self) -> int:
        res = self.lst[self.pointer]
        self.pointer += 1
        return res.getInteger()

    def hasNext(self) -> bool:
        return len(self.lst) > self.pointer


if __name__ == "__main__":
    nestedList = [[1, 1], 2, [1, 1]]
    nestedList = NestedInteger.to_nested(nestedList)
    obj = NestedIterator(nestedList.val)
    assert obj.next() == 1
    assert obj.next() == 1
    assert obj.next() == 2
    assert obj.hasNext() is True
    assert obj.next() == 1
    assert obj.next() == 1
    assert obj.hasNext() is False
