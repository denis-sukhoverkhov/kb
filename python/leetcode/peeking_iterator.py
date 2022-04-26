# Below is the interface for Iterator, which is already defined for you.
import copy


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.pointer = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.pointer < len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        result = self.nums[self.pointer]
        self.pointer += 1

        return result


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        # self.cached_current_value = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        current_iterator = copy.copy(self.iterator)
        return current_iterator.next()

    def next(self):
        """
        :rtype: int
        """
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """

        return self.iterator.hasNext()


if __name__ == "__main__":
    iterator = Iterator([1, 2, 3])
    peekingIterator = PeekingIterator(iterator)
    assert peekingIterator.next() == 1
    assert peekingIterator.peek() == 2
    assert peekingIterator.next() == 2
    assert peekingIterator.next() == 3
    assert peekingIterator.hasNext() is False
