# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, val):
        self.val = val

    def isInteger(self) -> bool:
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
        return isinstance(self.val, int)

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        if self.isInteger():
            return self.val

        return None

    def getList(self) -> ["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        if not self.isInteger():
            return self.val

        return None

    @classmethod
    def to_nested(cls, nestedList):

        def traversal(lst):
            if isinstance(lst, int):
                return NestedInteger(lst)

            res = NestedInteger(val=[])
            for i in lst:
                res.val.append(traversal(i))

            return res

        return traversal(nestedList)
