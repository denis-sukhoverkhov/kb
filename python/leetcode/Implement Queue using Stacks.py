class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        temp_stack = []
        while self.stack:
            temp_stack.append(self.stack.pop())

        self.stack.append(x)
        while temp_stack:
            self.stack.append(temp_stack.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:

        return self.stack[-1] if self.stack else None

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    assert myQueue.peek() == 1
    assert myQueue.pop() == 1
    assert myQueue.empty() is False
