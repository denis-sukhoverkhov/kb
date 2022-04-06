class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self._add_min_value(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_values.pop()

    def _add_min_value(self, val):
        if not self.min_values or val < self.min_values[-1]:
            self.min_values.append(val)
            return

        self.min_values.append(self.min_values[-1])

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
